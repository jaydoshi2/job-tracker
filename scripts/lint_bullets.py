#!/usr/bin/env python3
"""
Lint resume bullets against .claude/skills/tailor/references/bullet_guidelines.md.

  python3 scripts/lint_bullets.py applications/<app>/resume.tex            # text checks
  python3 scripts/lint_bullets.py applications/<app>/resume.tex --pdf      # + real one-line check

--pdf uses the compiled resume.pdf next to the .tex and `pdftotext -layout` (poppler) to
detect bullets that wrap onto a second line. Without pdftotext it falls back to a
character budget (--max-chars, default 128 ≈ one line in an 11pt Times Jake-style template).

Supports `\\item ...` and macro bullets like Jake's template `\\resumeItem{...}`.
Exit code 1 if any ERROR, else 0. Warnings never fail the run.
"""
import argparse
import re
import shutil
import subprocess
import sys
from collections import Counter
from pathlib import Path

STRONG_VERBS = set("""
architected built designed engineered implemented prototyped launched shipped deployed developed created
optimized accelerated reduced cut streamlined refactored scaled hardened boosted improved increased decreased
automated scripted orchestrated containerized migrated integrated consolidated standardized
analyzed benchmarked profiled diagnosed debugged modeled evaluated quantified forecasted identified
trained fine-tuned researched investigated validated published labeled curated
aggregated cleaned visualized queried indexed partitioned pipelined
led spearheaded mentored coordinated drove owned organized taught presented recruited
secured tested monitored instrumented audited patched resolved
delivered established generated achieved won earned awarded ranked authored wrote documented
redesigned rebuilt rewrote extended parallelized cached reverse-engineered simulated
collaborated partnered negotiated managed planned facilitated tutored supported maintained
""".split())
# Present-tense forms allowed for a current role (validated -> validate, analyzed -> analyze)
for _v in list(STRONG_VERBS):
    if _v.endswith("ed"):
        STRONG_VERBS.update({_v[:-2], _v[:-1]})
        if _v.endswith("ied"):
            STRONG_VERBS.add(_v[:-3] + "y")
PRESENT = {"build", "design", "engineer", "implement", "develop", "create", "optimize", "reduce", "lead",
           "automate", "analyze", "train", "research", "maintain", "manage", "mentor", "teach", "own",
           "drive", "debug", "test", "monitor", "write", "deploy", "ship", "scale", "migrate", "integrate", "tutor"}
STRONG_VERBS |= PRESENT

BANNED_OPENERS = ["responsible for", "duties included", "tasked with", "helped", "assisted", "aided",
                  "worked on", "participated in", "involved in", "was", "were", "utilized", "handled"]
FILLER = ["successfully", "effectively", "efficiently", "various", "numerous", "very", "really",
          "in order to", "a variety of", "hard-working", "team player", "detail-oriented", "synergy"]
FIRST_PERSON = re.compile(r"\b(i|me|my|our|we)\b", re.I)
METRIC = re.compile(r"\d|%|\bx\b|\bk\b|\bpercent\b|\b(first|second|third|top|two|three|four|five|six|"
                    r"seven|eight|nine|ten|dozen|hundreds?|thousands?|millions?)\b", re.I)


def strip_comments(tex):
    return "\n".join(re.sub(r"(?<!\\)%.*", "", ln) for ln in tex.splitlines())


def brace_arg(s, start):
    """Return content of the balanced {...} starting at s[start]=='{'."""
    depth, i = 0, start
    while i < len(s):
        if s[i] == "{" and (i == 0 or s[i - 1] != "\\"):
            depth += 1
        elif s[i] == "}" and s[i - 1] != "\\":
            depth -= 1
            if depth == 0:
                return s[start + 1:i]
        i += 1
    return s[start + 1:]


def extract_bullets(tex_raw):
    """Return raw LaTeX text of each bullet (comments kept so a stray % is detectable)."""
    body = tex_raw.split(r"\begin{document}", 1)[-1]
    body = "\n".join(l for l in body.splitlines() if not l.lstrip().startswith("%"))  # skip commented-out lines
    bullets = []
    macro_hits = list(re.finditer(r"\\resumeItem\s*(\{)", body))
    if macro_hits:
        for m in macro_hits:
            bullets.append(brace_arg(body, m.start(1)))
    else:
        for m in re.finditer(r"\\item\b(.*?)(?=\\item\b|\\end\{itemize\}|\\end\{enumerate\})", body, re.S):
            bullets.append(m.group(1))
    return [b.strip() for b in bullets if b.strip()]


def to_plain(raw):
    s = strip_comments(raw)
    s = re.sub(r"\\[vh]space\*?\{[^}]*\}", " ", s)          # spacing commands + their args
    s = re.sub(r"\$\\sim\$", "~", s)
    s = re.sub(r"\\(textbf|textit|emph|underline|texttt)\{([^{}]*)\}", r"\2", s)
    s = re.sub(r"\\href\{[^}]*\}\{([^{}]*)\}", r"\1", s)
    s = re.sub(r"\\([&%#_$])", r"\1", s)
    s = s.replace("--", "-").replace("\\\\", " ")
    s = re.sub(r"\\[a-zA-Z]+\*?", "", s)
    s = re.sub(r"[{}$]", "", s)
    return re.sub(r"\s+", " ", s).strip()


def escape_problems(raw):
    probs = []
    # remove math segments $...$ first
    no_math = re.sub(r"(?<!\\)\$[^$]*(?<!\\)\$", " ", raw)
    for ch, name in [("&", "&"), ("#", "#"), ("_", "_")]:
        if re.search(r"(?<!\\)" + re.escape(ch), no_math):
            probs.append(f"unescaped '{name}' (write \\{name})")
    if re.search(r"(?<!\\)%", raw):
        probs.append("unescaped '%' comments out the rest of the line (write \\%)")
    if re.search(r"(?<![\\$])~\s*\d", raw):
        probs.append("'~' before a number prints as a space (write $\\sim$)")
    if re.search(r"(?<!\$)[<>](?!\$)", no_math):
        probs.append("bare < or > may print as ¡ ¿ (write $<$ or $>$)")
    return probs


def is_label_line(plain):
    """Lines like 'Coursework: ...' or 'Languages: ...' are not achievement bullets."""
    head = plain.split(":", 1)[0]
    return ":" in plain and len(head) <= 30 and len(head.split()) <= 4


def _norm(t):
    t = t.replace("\ufb01", "fi").replace("\ufb02", "fl").replace("\ufb00", "ff")
    return re.sub(r"[^a-z0-9]", "", t.lower())


def wrapped_bullets_from_pdf(pdf, plain_bullets):
    """For each bullet, find the PDF line where it starts and count how many lines it spans.
    Works with any bullet glyph or template because it matches the bullet's own text."""
    out = subprocess.run(["pdftotext", "-layout", str(pdf), "-"], capture_output=True, text=True).stdout
    lines = [_norm(l) for l in out.splitlines()]
    results = []
    for text in plain_bullets:
        target = _norm(text)
        if len(target) < 12:
            continue
        head = target[:20]
        idx = next((i for i, l in enumerate(lines) if head in l), None)
        if idx is None:
            results.append((text[:60], -1))   # not found (e.g. hyphenation); report as unknown
            continue
        acc, n, j = lines[idx][lines[idx].index(head):], 1, idx + 1
        while target not in acc and j < len(lines) and n < 4:
            if lines[j]:                      # pdftotext inserts blank lines; skip them
                acc += lines[j]
                n += 1
            j += 1
        results.append((text[:60], n if target in acc else -1))
    return results


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("tex")
    ap.add_argument("--pdf", action="store_true", help="check real line wrapping in the compiled PDF")
    ap.add_argument("--max-chars", type=int, default=128)
    ap.add_argument("--metric-ratio", type=float, default=0.7)
    a = ap.parse_args()

    tex_path = Path(a.tex)
    raw = tex_path.read_text(encoding="utf-8")
    bullets = extract_bullets(raw)
    errors, warnings = [], []
    openers, achievement, with_metric = Counter(), 0, 0

    for n, b in enumerate(bullets, 1):
        plain = to_plain(b)
        tag = f"[{n}] \"{plain[:55]}{'…' if len(plain) > 55 else ''}\""
        for p in escape_problems(b):
            errors.append(f"{tag}: {p}")
        if is_label_line(plain):
            continue
        achievement += 1
        low = plain.lower()
        first = re.sub(r"[^a-z\-]", "", low.split()[0]) if low.split() else ""
        openers[first] += 1

        banned = next((o for o in BANNED_OPENERS if low.startswith(o + " ") or low == o), None)
        if banned:
            errors.append(f"{tag}: banned opener '{banned}'; start with a specific action verb")
        elif first.endswith("ing"):
            errors.append(f"{tag}: starts with '-ing' verb; use a past-tense verb instead")
        elif first not in STRONG_VERBS:
            warnings.append(f"{tag}: opener '{first}' isn't in the verb bank; check it's a strong action verb")
        if FIRST_PERSON.search(plain):
            errors.append(f"{tag}: first-person pronoun; the subject is implied")
        for f in FILLER:
            if re.search(r"\b" + re.escape(f) + r"\b", low):
                warnings.append(f"{tag}: filler '{f}'; delete it (the number proves it)")
        if METRIC.search(plain):
            with_metric += 1
        else:
            warnings.append(f"{tag}: no number or scope; add one if the experience bank has it")
        if not a.pdf and len(plain) > a.max_chars:
            errors.append(f"{tag}: {len(plain)} chars > {a.max_chars}; likely wraps to 2 lines")

    for verb, c in openers.items():
        if c > 2:
            errors.append(f"opener '{verb}' used {c} times; max 2 per page, vary your verbs")
    if achievement and with_metric / achievement < a.metric_ratio:
        warnings.append(f"only {with_metric}/{achievement} bullets have a number (target ≥{int(a.metric_ratio*100)}%)")

    if a.pdf:
        pdf = tex_path.with_suffix(".pdf")
        if not pdf.exists():
            errors.append(f"{pdf.name} not found; run build_resume.py first")
        elif not shutil.which("pdftotext"):
            warnings.append("pdftotext not installed; using character budget instead (install poppler)")
            for n, b in enumerate(bullets, 1):
                plain = to_plain(b)
                if not is_label_line(plain) and len(plain) > a.max_chars:
                    errors.append(f"[{n}] \"{plain[:55]}…\": {len(plain)} chars > {a.max_chars}; likely wraps")
        else:
            plains = [to_plain(b) for b in bullets if not is_label_line(to_plain(b))]
            for text, nlines in wrapped_bullets_from_pdf(pdf, plains):
                if nlines > 1:
                    errors.append(f"\"{text}…\" wraps to {nlines} lines in the PDF; trim it to one line")
                elif nlines == -1:
                    warnings.append(f"\"{text}…\" couldn't be located in the PDF; check its length by eye")

    print(f"BULLET LINT: {len(bullets)} bullets ({achievement} achievement) | "
          f"{len(errors)} errors | {len(warnings)} warnings")
    for e in errors:
        print("  ERROR  " + e)
    for w in warnings:
        print("  warn   " + w)
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()

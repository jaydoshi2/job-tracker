#!/usr/bin/env python3
"""
Deterministic ATS-style scorer.

Claude does the judgment step once per job (writing keywords.json from the JD).
This script then scores ANY resume against that same keywords.json, so the
before/after numbers are reproducible and comparable.

Usage:
  python3 scripts/ats_score.py --keywords applications/<app>/keywords.json \
                               --resume master/resume.tex [--json]

keywords.json schema:
{
  "title": "Software Engineer Intern",
  "required":  [{"term": "Python", "aliases": ["py"]}, ...],
  "preferred": [{"term": "Kubernetes", "aliases": ["k8s"]}, ...]
}
"""
import argparse
import json
import re
import sys
from pathlib import Path

WEIGHTS = {"required": 50, "preferred": 20, "title": 10, "format": 20}
STANDARD_SECTIONS = ["education", "experience", "skills", "projects"]
RISKY_LATEX = {
    r"\\includegraphics": "images/graphics are invisible to most ATS parsers",
    r"\\begin\{multicols\}": "multi-column layouts often get read out of order",
    r"\\begin\{minipage\}": "side-by-side boxes can scramble reading order",
    r"\\fa[A-Z]\w*|\\faIcon": "icon fonts turn into garbage characters when parsed",
}


def latex_to_text(tex: str) -> str:
    """Rough LaTeX -> plain text, good enough for keyword matching."""
    tex = re.sub(r"(?<!\\)%.*", "", tex)                       # comments
    body = tex.split(r"\begin{document}", 1)[-1]                # skip preamble
    body = re.sub(r"\\(href|url)\{[^}]*\}", " ", body)          # link targets
    body = re.sub(r"\\[a-zA-Z@]+\*?(\[[^\]]*\])?", " ", body)   # commands
    body = body.replace("\\&", "&").replace("\\%", "%").replace("\\#", "#")
    body = body.replace("\\_", "_").replace("\\$", "$")
    body = re.sub(r"[{}~\\]", " ", body)
    return re.sub(r"\s+", " ", body).strip()


def term_regex(term: str) -> re.Pattern:
    # Boundaries that survive terms like C++, C#, .NET, Node.js, CI/CD
    return re.compile(r"(?<![A-Za-z0-9])" + re.escape(term.lower()) + r"(?![A-Za-z0-9+#])")


def found(item, text_lower: str) -> bool:
    terms = [item["term"]] + item.get("aliases", [])
    return any(term_regex(t).search(text_lower) for t in terms)


def coverage(items, text_lower):
    hits = [i["term"] for i in items if found(i, text_lower)]
    misses = [i["term"] for i in items if not found(i, text_lower)]
    ratio = len(hits) / len(items) if items else 1.0
    return ratio, hits, misses


def format_checks(tex: str, text_lower: str):
    points, notes = 0.0, []
    present = [s for s in STANDARD_SECTIONS if s in text_lower]
    points += 10 * len(present) / len(STANDARD_SECTIONS)
    missing = sorted(set(STANDARD_SECTIONS) - set(present))
    if missing:
        notes.append(f"Missing standard section headers: {', '.join(missing)}")
    if re.search(r"[\w.+-]+@[\w-]+\.[\w.]+", tex):
        points += 5
    else:
        notes.append("No email address detected")
    risky = [why for pat, why in RISKY_LATEX.items() if re.search(pat, tex)]
    points += 5 if not risky else max(0, 5 - 2 * len(risky))
    notes.extend(risky)
    return points, notes


def score(keywords: dict, tex: str) -> dict:
    text_lower = latex_to_text(tex).lower()
    req_r, req_hit, req_miss = coverage(keywords.get("required", []), text_lower)
    pref_r, pref_hit, pref_miss = coverage(keywords.get("preferred", []), text_lower)

    title_words = [w for w in re.findall(r"[a-z]+", keywords.get("title", "").lower())
                   if w not in {"intern", "internship", "summer", "the", "and", "of", "i", "ii"}]
    title_r = (sum(1 for w in title_words if term_regex(w).search(text_lower)) / len(title_words)
               if title_words else 1.0)

    fmt_pts, fmt_notes = format_checks(tex, text_lower)
    breakdown = {
        "required": round(WEIGHTS["required"] * req_r, 1),
        "preferred": round(WEIGHTS["preferred"] * pref_r, 1),
        "title": round(WEIGHTS["title"] * title_r, 1),
        "format": round(fmt_pts, 1),
    }
    return {
        "score": round(sum(breakdown.values())),
        "breakdown": breakdown,
        "required_matched": req_hit, "required_missing": req_miss,
        "preferred_matched": pref_hit, "preferred_missing": pref_miss,
        "format_notes": fmt_notes,
        "word_count": len(text_lower.split()),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--keywords", required=True)
    ap.add_argument("--resume", required=True)
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    a = ap.parse_args()

    try:
        keywords = json.loads(Path(a.keywords).read_text(encoding="utf-8"))
        tex = Path(a.resume).read_text(encoding="utf-8")
    except (OSError, json.JSONDecodeError) as e:
        sys.exit(f"Error reading inputs: {e}")

    r = score(keywords, tex)
    if a.json:
        print(json.dumps(r, indent=2))
        return
    b = r["breakdown"]
    print(f"ATS SCORE: {r['score']}/100")
    print(f"  Required  {b['required']:>5}/{WEIGHTS['required']}   Preferred {b['preferred']:>5}/{WEIGHTS['preferred']}")
    print(f"  Title     {b['title']:>5}/{WEIGHTS['title']}   Format    {b['format']:>5}/{WEIGHTS['format']}")
    print(f"  Missing required : {', '.join(r['required_missing']) or 'none'}")
    print(f"  Missing preferred: {', '.join(r['preferred_missing']) or 'none'}")
    for n in r["format_notes"]:
        print(f"  Format note: {n}")


if __name__ == "__main__":
    main()

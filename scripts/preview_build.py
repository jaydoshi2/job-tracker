#!/usr/bin/env python3
"""
Compile a PREVIEW of an Overleaf resume in the sandbox so line wrapping can be measured.

Overleaf has every LaTeX package; the sandbox may not. This script swaps missing
packages for metric-compatible stand-ins (e.g. newtx Times -> mathptmx Times, which
has the same character widths), stubs icon commands, compiles, and reports pages.
The preview is ONLY for measuring; the user's real .tex is never modified.

  python3 preview_build.py resume.tex        -> writes resume.preview.pdf next to it
Exit: 0 ok · 1 LaTeX error · 2 more than one page · 3 pdflatex unavailable (use char budget)
"""
import re
import shutil
import subprocess
import sys
from pathlib import Path

# package -> replacement preamble line (empty string = drop it)
SUBSTITUTES = {
    "newtxtext": r"\usepackage{mathptmx}",           # Times, same metrics
    "newtxmath": "",
    "fontawesome5": "", "fontawesome": "",
    "ulem": "", "academicons": "", "charter": "",
}
ICON_STUBS = r"""
\providecommand{\faAt}{@}\providecommand{\faEnvelope}{}\providecommand{\faPhone}{}
\providecommand{\faLinkedin}{}\providecommand{\faGithub}{}\providecommand{\faGlobe}{}
\providecommand{\faMapMarker}{}\providecommand{\faMobile}{}\providecommand{\uline}[1]{#1}
"""


def available(pkg):
    return subprocess.run(["kpsewhich", pkg + ".sty"], capture_output=True, text=True).stdout.strip() != ""


def make_preview(tex: str) -> str:
    def repl(m):
        opts, pkgs = m.group(1) or "", [p.strip() for p in m.group(2).split(",")]
        keep, extra = [], []
        for p in pkgs:
            if p in SUBSTITUTES and not available(p):
                if SUBSTITUTES[p]:
                    extra.append(SUBSTITUTES[p])
            elif available(p) or p == "":
                keep.append(p)
        line = f"\\usepackage{opts}{{{','.join(keep)}}}" if keep else ""
        return "\n".join([line] + extra)
    tex = re.sub(r"\\usepackage(\[[^\]]*\])?\{([^}]*)\}", repl, tex)
    return tex.replace(r"\begin{document}", ICON_STUBS + "\n\\begin{document}", 1)


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    src = Path(sys.argv[1]).resolve()
    if not shutil.which("pdflatex"):
        print("NO PDFLATEX: use lint_bullets.py without --pdf (character budget).")
        sys.exit(3)
    prev = src.with_name(src.stem + ".preview.tex")
    prev.write_text(make_preview(src.read_text(encoding="utf-8")), encoding="utf-8")
    proc = None
    for _ in range(2):
        proc = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error", prev.name],
                              cwd=prev.parent, capture_output=True, text=True)
        if proc.returncode:
            break
    log = prev.with_suffix(".log").read_text(errors="ignore") if prev.with_suffix(".log").exists() else ""
    if proc.returncode:
        print("PREVIEW BUILD FAILED (often a real LaTeX bug, e.g. unescaped & or %):")
        for i, l in enumerate(log.splitlines()):
            if l.startswith("!"):
                print("  " + l)
        sys.exit(1)
    m = re.search(r"Output written on .*?\((\d+) pages?", log)
    pages = int(m.group(1)) if m else -1
    for ext in (".aux", ".log", ".out"):
        prev.with_suffix(ext).unlink(missing_ok=True)
    print(f"PREVIEW OK: {prev.with_suffix('.pdf').name} | pages: {pages}")
    if pages > 1:
        print("TOO LONG: more than one page. Cut the least relevant bullet.")
        sys.exit(2)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Compile a resume to PDF and check it is one page.

  python3 scripts/build_resume.py applications/<app>/resume.tex

1. Tries a real pdflatex build -> resume.pdf (the file you upload).
2. If your TeX install is missing a package (fontawesome5, newtx, ulem...), it builds a
   look-alike PREVIEW instead (scripts/preview_build.py) so line wrapping can still be
   checked, and tells you how to install the package or to compile in Overleaf.

Last line printed is always `LINT TARGET: <tex file>`: run lint_bullets.py on that file.
Exit: 0 ok · 1 LaTeX error · 2 over one page · 3 no pdflatex at all
"""
import re
import shutil
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent


def compile_tex(tex: Path):
    proc = None
    for _ in range(2):
        proc = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error", tex.name],
                              cwd=tex.parent, capture_output=True, text=True)
        if proc.returncode:
            break
    log_path = tex.with_suffix(".log")
    log = log_path.read_text(errors="ignore") if log_path.exists() else proc.stdout
    return proc.returncode, log


def cleanup(tex: Path):
    for ext in (".aux", ".log", ".out", ".fls", ".fdb_latexmk"):
        tex.with_suffix(ext).unlink(missing_ok=True)


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    tex = Path(sys.argv[1]).resolve()
    if not tex.exists():
        sys.exit(f"{tex} not found")
    if not shutil.which("pdflatex"):
        print("pdflatex not found. Install LaTeX (GUIDE Step 1) or compile in Overleaf.")
        print(f"LINT TARGET: {tex}  (no PDF; lint will use the character budget)")
        sys.exit(3)

    code, log = compile_tex(tex)
    missing = re.findall(r"File `([^']+\.sty)' not found", log)
    if code and missing:
        # list EVERY missing package in the preamble, not just the first one LaTeX hit
        used = set()
        for grp in re.findall(r"\\usepackage(?:\[[^\]]*\])?\{([^}]*)\}", tex.read_text(errors="ignore")):
            used.update(x.strip() for x in grp.split(","))
        absent = {u for u in used if u and not subprocess.run(["kpsewhich", u + ".sty"],
                  capture_output=True, text=True).stdout.strip()}
        absent |= {m[:-4] for m in missing}
        # tlmgr package names differ for a few
        names = {"newtxtext": "newtx", "newtxmath": "newtx"}
        pkgs = " ".join(sorted({names.get(a, a) for a in absent}))
        print(f"Your LaTeX install is missing: {pkgs}")
        print(f"  Fix once:  sudo tlmgr install {pkgs}   (MiKTeX installs them automatically)")
        print("  Meanwhile building a look-alike preview to check line wrapping...")
        cleanup(tex)
        r = subprocess.run([sys.executable, str(HERE / "preview_build.py"), str(tex)],
                           capture_output=True, text=True)
        print("  " + r.stdout.strip().replace("\n", "\n  "))
        print("  Upload a PDF compiled in Overleaf (paste resume.tex there) until the package is installed.")
        print(f"LINT TARGET: {tex.with_name(tex.stem + '.preview.tex')}")
        sys.exit(r.returncode)

    if code:
        print("BUILD FAILED. LaTeX errors:")
        lines = log.splitlines()
        for i, line in enumerate(lines):
            if line.startswith("!"):
                print("  " + " ".join(l.strip() for l in lines[i:i + 3]))
        cleanup(tex)
        print(f"LINT TARGET: {tex}")
        sys.exit(1)

    m = re.search(r"Output written on .*?\((\d+) pages?", log)
    pages = int(m.group(1)) if m else -1
    cleanup(tex)
    print(f"BUILD OK: {tex.with_suffix('.pdf').name} | pages: {pages}")
    if pages > 1:
        print("TOO LONG: more than one page. Comment out the least relevant bullet.")
    print(f"LINT TARGET: {tex}")
    if pages > 1:
        sys.exit(2)


if __name__ == "__main__":
    main()

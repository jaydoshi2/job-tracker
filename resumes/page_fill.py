#!/usr/bin/env python3
"""
Measure how much empty space is left at the bottom of a one-page LaTeX resume.

LaTeX itself reports the exact numbers: a copy of the .tex gets
  \\par\\typeout{PAGEFILL \\the\\pagetotal|\\the\\pagegoal}
injected right before \\end{document}; pagegoal - pagetotal = unused height.
That height is converted to "bullet lines" using the real bullet pitch measured
from the compiled PDF (vertical distance between consecutive bullets).

  python3 page_fill.py resume.tex            (pass the .preview.tex if you use preview_build.py)
  python3 page_fill.py resume.tex --json

Exit: 0 page is full (less than one bullet line free)
      1 LaTeX error
      2 more than one page (cut the least relevant bullet)
      3 pdflatex unavailable
      4 UNDERFILLED: at least one more one-line bullet fits -> add content
The real .tex is never modified; all work happens in a temp folder.
"""
import argparse
import json
import re
import shutil
import statistics
import subprocess
import sys
import tempfile
from pathlib import Path

PT_PER_BP = 72.27 / 72  # TeX points per PDF point
DEFAULT_PITCH_BP = 16.5  # Jake-style 11pt resume, used if the PDF can't be measured


def measure_pitch(pdf_path):
    """Median vertical distance (PDF points) between consecutive bullets in the same column."""
    try:
        import pdfplumber
    except ImportError:
        return None
    try:
        with pdfplumber.open(str(pdf_path)) as pdf:
            chars = pdf.pages[0].chars
    except Exception:
        return None
    bullets = sorted({round(c["top"], 1) for c in chars if c["text"] in ("•", "∙", "·", "\u2022")})
    gaps = [b - a for a, b in zip(bullets, bullets[1:]) if 8 < b - a < 30]
    if len(gaps) >= 3:
        return statistics.median(gaps)
    # Fallback: bullet glyphs often have no unicode mapping (CMSY), so use the
    # spacing between consecutive text lines, which is dominated by bullet rows.
    tops = []
    for t in sorted(round(c["top"], 1) for c in chars):
        if not tops or t - tops[-1] > 2:
            tops.append(t)
    gaps = [b - a for a, b in zip(tops, tops[1:]) if 10 < b - a < 25]
    return statistics.median(gaps) if len(gaps) >= 3 else None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("tex")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--pitch", type=float, help="override bullet pitch in PDF points")
    args = ap.parse_args()

    src = Path(args.tex).resolve()
    if not shutil.which("pdflatex"):
        print("NO PDFLATEX: estimate fill from the last compiled PDF instead.")
        sys.exit(3)

    tex = src.read_text(encoding="utf-8")
    probe = r"\par\typeout{PAGEFILL \the\pagetotal|\the\pagegoal|\the\baselineskip}" + "\n"
    if r"\end{document}" not in tex:
        print("No \\end{document} found.")
        sys.exit(1)
    tex = tex.replace(r"\end{document}", probe + r"\end{document}", 1)

    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        # copy sibling files (class files, images, \input'ed parts) so the build behaves the same
        for f in src.parent.iterdir():
            if f.is_file() and f.suffix in (".cls", ".sty", ".tex", ".png", ".jpg", ".pdf", ".bib"):
                shutil.copy(f, tmp / f.name)
        probe_tex = tmp / "fillprobe.tex"
        probe_tex.write_text(tex, encoding="utf-8")
        proc = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error", probe_tex.name],
                              cwd=tmp, capture_output=True, text=True)
        log = (tmp / "fillprobe.log").read_text(errors="ignore") if (tmp / "fillprobe.log").exists() else ""
        if proc.returncode:
            print("BUILD FAILED:")
            for line in log.splitlines():
                if line.startswith("!"):
                    print("  " + line)
            sys.exit(1)
        pages_m = re.search(r"Output written on .*?\((\d+) pages?", log)
        pages = int(pages_m.group(1)) if pages_m else -1
        m = re.search(r"PAGEFILL ([\d.]+)pt\|([\d.]+)pt\|([\d.]+)pt", log)
        pitch_bp = args.pitch or measure_pitch(tmp / "fillprobe.pdf")

    if pages > 1:
        print(f"TOO LONG: {pages} pages. Cut the least relevant bullet.")
        sys.exit(2)
    if not m:
        print("Could not read PAGEFILL from the log (a \\vfill or float may hide it).")
        sys.exit(0)

    total, goal, _ = (float(x) for x in m.groups())
    free_pt = max(goal - total, 0.0)
    measured = pitch_bp is not None
    pitch_pt = (pitch_bp or DEFAULT_PITCH_BP) * PT_PER_BP
    free_lines = free_pt / pitch_pt
    fill_pct = 100 * total / goal if goal else 0
    result = {
        "pages": pages,
        "used_pt": round(total, 1), "page_goal_pt": round(goal, 1),
        "free_pt": round(free_pt, 1), "fill_pct": round(fill_pct, 1),
        "bullet_pitch_pt": round(pitch_pt, 1), "pitch_measured": measured,
        "free_bullet_lines": round(free_lines, 2),
        "bullets_to_add": int(free_lines),
        "status": "UNDERFILLED" if free_lines >= 1 else "FULL",
    }
    if args.json:
        print(json.dumps(result))
    else:
        print(f"PAGE FILL: {fill_pct:.1f}% · free {free_pt:.1f}pt ≈ {free_lines:.1f} bullet lines "
              f"(pitch {pitch_pt:.1f}pt{'' if measured else ', default'})")
        if free_lines >= 1:
            print(f"UNDERFILLED: add {int(free_lines)} one-line bullet(s) from the bank "
                  f"(see SKILL.md Step 6b fill order).")
        else:
            print("FULL: less than one bullet line free.")
    sys.exit(4 if free_lines >= 1 else 0)


if __name__ == "__main__":
    main() 
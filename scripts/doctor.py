#!/usr/bin/env python3
"""Check every setup step in GUIDE.md.   Run:  python3 scripts/doctor.py"""
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ok_all = True


def check(label, ok, fix=""):
    global ok_all
    print(f"  {'✅' if ok else '❌'} {label}" + ("" if ok or not fix else f"\n       → {fix}"))
    ok_all &= bool(ok)


def run(cmd):
    try:
        return subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True, timeout=180)
    except (OSError, subprocess.TimeoutExpired):
        return None


print("Step 1 · Tools")
check("Python 3.9+", sys.version_info >= (3, 9), "Install Python 3.9+")
for tool, fix in [("git", "Install Git"),
                  ("pdflatex", "Install MacTeX (full) / MiKTeX / texlive-full"),
                  ("pdftotext", "brew install poppler · choco install poppler · apt install poppler-utils"),
                  ("claude", "Install Claude Code (GUIDE Step 1)")]:
    check(tool, shutil.which(tool), fix)

print("Step 2 · GitHub repo")
r = run(["git", "remote", "get-url", "origin"])
check("git remote 'origin' set", r and r.returncode == 0 and r.stdout.strip(),
      "git remote add origin https://github.com/<you>/job-tracker.git")

print("Step 3 · Your resumes")
files = ["resume_ai.tex", "resume_datascience.tex", "resume_network.tex", "resume_software.tex", "projects_bank.tex"]
for f in files:
    p = ROOT / "resumes" / f
    check(f"resumes/{f}", p.exists() and r"\begin{document}" in p.read_text(errors="ignore"),
          "Copy this file's full source from Overleaf (Menu → Download → Source, or copy-paste)")

print("Step 4 · Each resume compiles (real PDF or preview)")
if shutil.which("pdflatex"):
    for f in files[:4]:
        p = ROOT / "resumes" / f
        if not p.exists():
            continue
        r = run([sys.executable, "scripts/build_resume.py", str(p)])
        out = r.stdout if r else ""
        mode = "real PDF" if "BUILD OK" in out else "preview only" if "PREVIEW OK" in out else "failed"
        check(f"{f}: {mode}", r and r.returncode == 0,
              out.strip().splitlines()[0] if out.strip() else "build failed")
        if mode == "preview only":
            print("       (works; install the missing packages listed by build_resume.py for real PDFs)")
        for junk in p.parent.glob(p.stem + "*.p*"):
            if junk.suffix in {".pdf"} or ".preview" in junk.name:
                junk.unlink(missing_ok=True)

print("Step 5 · Claude Code project files")
for f in [".claude/skills/tailor/SKILL.md", ".claude/skills/tailor/references/bullet_guidelines.md",
          ".claude/skills/status/SKILL.md", "CLAUDE.md", ".claude/settings.json",
          "tracker/applications.csv"]:
    check(f, (ROOT / f).exists(), "Missing; re-copy from the zip")

print("\n" + ("🎉 All set. Run `claude` here and paste a job description."
              if ok_all else "Fix the ❌ items, then run this again."))
sys.exit(0 if ok_all else 1)

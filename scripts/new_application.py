#!/usr/bin/env python3
"""
Create a new application folder with a fresh copy of the master resume.

  python3 scripts/new_application.py --track ai --company "Google" --role "ML Intern"
  -> copies resumes/resume_ai.tex into a new folder and prints its path,
     e.g. applications/2026-10-04_google_ml-intern
Tracks: ai | datascience | network | software
"""
import argparse
import re
import shutil
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def slug(s, n=40):
    s = re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")
    return s[:n].rstrip("-") or "unknown"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--company", required=True)
    ap.add_argument("--role", required=True)
    ap.add_argument("--track", required=True, choices=["ai", "datascience", "network", "software"])
    a = ap.parse_args()

    master = ROOT / "resumes" / f"resume_{a.track}.tex"
    if not master.exists():
        sys.exit(f"{master.relative_to(ROOT)} not found. Copy it from Overleaf first (GUIDE Step 3).")

    base = ROOT / "applications" / f"{date.today().isoformat()}_{slug(a.company, 25)}_{slug(a.role)}"
    folder, i = base, 2
    while folder.exists():
        folder = base.with_name(f"{base.name}-{i}")
        i += 1
    folder.mkdir(parents=True)
    shutil.copy(master, folder / "resume.tex")
    print(folder.relative_to(ROOT))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Job application tracker (tracker/applications.csv).

  python3 scripts/tracker.py exists --company "Google" [--req-id R123] [--role "SWE Intern"]
  python3 scripts/tracker.py add --company "Google" --role "SWE Intern" --resume-track ai [--field value ...]
      (status defaults to Applied: pasting a JD means you applied)
  python3 scripts/tracker.py update --id APP-0007 --status "Interview" [--notes "..."]
  python3 scripts/tracker.py update --company "Google" --status "Applied"   (most recent matching row)
  python3 scripts/tracker.py list [--status Applied] [--due]     (--due = follow-ups due today or earlier)
"""
import argparse
import csv
import sys
from datetime import date, timedelta
from pathlib import Path

CSV_PATH = Path(__file__).resolve().parent.parent / "tracker" / "applications.csv"
FIELDS = ["app_id", "date_applied", "company", "role", "req_id", "location",
          "work_mode", "season", "source", "job_url", "deadline", "resume_track", "ats_before", "ats_after",
          "folder", "keywords_added", "status", "status_updated",
          "follow_up_date", "referral_contact", "sponsorship", "pay", "notes"]
STATUSES = ["Applied", "OA", "Recruiter Screen", "Interview",
            "Final Round", "Offer", "Accepted", "Rejected", "Ghosted", "Withdrawn"]
FOLLOW_UP_DAYS = 14


def load():
    if not CSV_PATH.exists():
        return []
    with CSV_PATH.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def save(rows):
    CSV_PATH.parent.mkdir(parents=True, exist_ok=True)
    with CSV_PATH.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS, lineterminator="\n")
        w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k, "") for k in FIELDS})


def norm(s):
    return " ".join((s or "").lower().split())


def find_matches(rows, company, req_id=None, role=None):
    out = []
    for r in rows:
        if norm(r["company"]) != norm(company):
            continue
        if req_id and r.get("req_id") and norm(r["req_id"]) == norm(req_id):
            out.append(r)
        elif role and norm(r["role"]) == norm(role):
            out.append(r)
        elif not req_id and not role:
            out.append(r)
    return out


def check_status(s):
    match = next((x for x in STATUSES if x.lower() == s.lower()), None)
    if not match:
        sys.exit(f"Unknown status '{s}'. Use one of: {', '.join(STATUSES)}")
    return match


def apply_status(row, status):
    today = date.today().isoformat()
    row["status"] = status
    row["status_updated"] = today
    if status == "Applied":
        row["date_applied"] = row.get("date_applied") or today
        row["follow_up_date"] = (date.today() + timedelta(days=FOLLOW_UP_DAYS)).isoformat()
    elif status in {"Offer", "Accepted", "Rejected", "Withdrawn"}:
        row["follow_up_date"] = ""


def fmt(r):
    return (f"{r['app_id']} | {r['company']} | {r['role']} | {r['status']} | "
            f"ATS {r.get('ats_before') or '?'}->{r.get('ats_after') or '?'} | follow-up {r.get('follow_up_date') or '-'}")


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)

    e = sub.add_parser("exists")
    e.add_argument("--company", required=True)
    e.add_argument("--req-id")
    e.add_argument("--role")

    a = sub.add_parser("add")
    for f in FIELDS:
        if f not in {"app_id", "status_updated"}:
            a.add_argument("--" + f.replace("_", "-"), dest=f, default="")
    a.add_argument("--force", action="store_true", help="add even if a duplicate exists")

    u = sub.add_parser("update")
    u.add_argument("--id")
    u.add_argument("--company")
    for f in FIELDS:
        if f not in {"app_id", "company"}:
            u.add_argument("--" + f.replace("_", "-"), dest=f, default=None)

    l = sub.add_parser("list")
    l.add_argument("--status")
    l.add_argument("--due", action="store_true")

    args = ap.parse_args()
    rows = load()

    if args.cmd == "exists":
        m = find_matches(rows, args.company, args.req_id, args.role)
        if m:
            print("DUPLICATE FOUND:")
            for r in m:
                print("  " + fmt(r))
            sys.exit(1)
        print("No existing application found.")

    elif args.cmd == "add":
        if not args.company or not args.role:
            sys.exit("--company and --role are required")
        dupes = find_matches(rows, args.company, args.req_id or None, args.role)
        if dupes and not args.force:
            print("Not added; possible duplicate (use --force to override):")
            for r in dupes:
                print("  " + fmt(r))
            sys.exit(1)
        row = {f: getattr(args, f, "") or "" for f in FIELDS}
        row["app_id"] = f"APP-{len(rows) + 1:04d}"
        apply_status(row, check_status(args.status or "Applied"))
        rows.append(row)
        save(rows)
        print("ADDED: " + fmt(row))

    elif args.cmd == "update":
        if args.id:
            targets = [r for r in rows if r["app_id"] == args.id]
        elif args.company:
            targets = find_matches(rows, args.company)[-1:]
        else:
            sys.exit("Give --id or --company")
        if not targets:
            sys.exit("No matching application found.")
        row = targets[0]
        for f in FIELDS:
            val = getattr(args, f, None)
            if val is None or f == "status":
                continue
            if f == "notes" and row.get("notes"):
                row[f] = f"{row['notes']} | {date.today().isoformat()}: {val}"  # append, never overwrite
            elif f == "notes":
                row[f] = f"{date.today().isoformat()}: {val}"
            else:
                row[f] = val
        if args.status:
            apply_status(row, check_status(args.status))
        save(rows)
        print("UPDATED: " + fmt(row))

    elif args.cmd == "list":
        today = date.today().isoformat()
        sel = rows
        if args.status:
            sel = [r for r in sel if norm(r["status"]) == norm(args.status)]
        if args.due:
            sel = [r for r in sel if r.get("follow_up_date") and r["follow_up_date"] <= today]
        for r in sel:
            print(fmt(r))
        counts = {}
        for r in rows:
            counts[r["status"]] = counts.get(r["status"], 0) + 1
        print(f"\nTotal {len(rows)} | " + " | ".join(f"{k}: {v}" for k, v in counts.items()))


if __name__ == "__main__":
    main()

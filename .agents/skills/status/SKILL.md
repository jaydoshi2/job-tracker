---
name: status
description: Update or review my job applications. Use when I report news about an application ("got an OA from X", "rejected by Y", "interview with Z", "offer from W"), or ask "what's my pipeline", "what follow-ups are due", "how many applications have I sent".
argument-hint: "[<company> <news>]  or  [summary | due]"
---

# Application status

Input: $ARGUMENTS

Statuses: Applied, OA, Recruiter Screen, Interview, Final Round, Offer, Accepted, Rejected, Ghosted, Withdrawn.

**Update** (I name a company + news):
1. Map my words: "HackerRank"/"online assessment" → OA · "phone screen" → Recruiter Screen ·
   "superday"/"onsite" → Final Round.
2. Find the row: `python3 scripts/tracker.py list` (if several match, use role or ask).
3. `python3 scripts/tracker.py update --id <ID> --status "<Status>" --notes "<short note>"`
   (notes are appended with today's date).
4. No commit: `tracker/` is gitignored (private). Never push application data.
5. Reply in one line. For OA/Interview, offer to prep me from that application's `jd.md` and `changes.md`.

**Review** (empty input, "summary", "pipeline", or "due"):
- `python3 scripts/tracker.py list` and `python3 scripts/tracker.py list --due`
- Reply: totals by status, follow-ups due today (company + role), and Applied rows older than
  30 days with no update (suggest marking Ghosted).

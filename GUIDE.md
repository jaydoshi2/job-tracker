# Step-by-Step Guide: Job Applications with Claude Code

**What you'll have at the end:** paste a job description into Claude Code and it will
pick your AI / Data Science / Network / Software resume, tweak only bullets, skills and
projects (layout untouched), check every bullet fits on one line, compile the PDF, log the
job as **Applied** in `tracker/applications.csv`, and commit + push to GitHub. One message.

Each step ends with **✔ Done when**. Run `python3 scripts/doctor.py` anytime to see what's left.
Total setup: about 45 minutes.

---

## Phase A: One-time setup

### Step 1: Install the tools (15 min)

| Tool | Mac | Windows | Linux |
|---|---|---|---|
| Python 3.9+ | preinstalled, or python.org | python.org (tick "Add to PATH") | `sudo apt install python3` |
| Git | `xcode-select --install` | git-scm.com (includes Git Bash) | `sudo apt install git` |
| LaTeX | **MacTeX full** (tug.org/mactex) | **MiKTeX** (miktex.org) | `sudo apt install texlive-full` |
| pdftotext | `brew install poppler` | `choco install poppler` | `sudo apt install poppler-utils` |
| Claude Code | see code.claude.com/docs (native installer, or `npm install -g @anthropic-ai/claude-code`) | same | same |

Claude Code needs a Claude Pro/Max plan (or API key); it asks you to log in the first time.
Your template uses `fontawesome5`, `newtx` and `ulem`. MacTeX full, MiKTeX and texlive-full
include them. With a smaller install (BasicTeX), run once:
`sudo tlmgr install fontawesome5 newtx ulem`

Check:
```bash
python3 --version && git --version && pdflatex --version && pdftotext -v && claude --version
```
**✔ Done when** every command prints a version.

---

### Step 2: Create the GitHub repo (5 min)

1. Unzip `job-tracker.zip` somewhere permanent, e.g. `~/projects/job-tracker`.
2. On github.com → **New repository** → name `job-tracker` → **Private** → no README → Create.
3. In a terminal:
```bash
cd ~/projects/job-tracker
git init
git add .
git commit -m "setup"
git branch -M main
git remote add origin https://github.com/jaydoshi2/job-tracker.git
git push -u origin main
```
The first push asks you to sign in (browser popup or `gh auth login`). After that, Claude Code
pushes without asking. Claude Code uses **your** git login, so there are no connector permissions involved.

**✔ Done when** your files show on github.com with a 🔒 Private badge.

---

### Step 3: Add your five resume files (5 min)

From Overleaf, copy the full source of each into `resumes/` with these exact names:

| Your Overleaf resume | Save as |
|---|---|
| AI resume | `resumes/resume_ai.tex` |
| Data Science resume | `resumes/resume_datascience.tex` |
| Network Engineering resume | `resumes/resume_network.tex` |
| Software resume | `resumes/resume_software.tex` |
| Projects file (the long one with all projects) | `resumes/projects_bank.tex` |

Then commit them:
```bash
git add resumes && git commit -m "add master resumes" && git push
```
**✔ Done when** `python3 scripts/doctor.py` shows ✅ for Steps 3 and 4.
("preview only" in Step 4 means a LaTeX package is missing; it still works, see Step 1.)

---

### Step 4: Fix conflicting facts in your files (10 min)

Claude treats `resumes/` as the truth, so one fact must have one version. In your current
files, fix these once:

- Cleveland-Cliffs title: "Process Automation Intern" vs "Data Processing Engineer Intern".
  Use your official title in all four (background checks verify titles).
- Cenovus end date: "Present" vs "Present".
- SportsSight dates: Jan–Apr 2025 vs Aug–Dec 2024.
- DeepTruth: "1,000+ users" vs "tested with 50+ users"; "Won RocketHacks" vs
  "1st place, Best Use of MongoDB" (a category win isn't the overall win).
- Chat app: 300+ students vs 200+ concurrent.
- Project links in `projects_bank.tex`: SportsSight points to the DeepTruth repo,
  Multi-Agent's "Github Link" goes to Google Drive, BCD points to github.com.

Every skill in any file can be added to a tailored resume, so keep only skills you can
discuss in an interview. Commit when done.

**✔ Done when** each fact reads the same in every file.

---

### Step 5: Open Claude Code in the repo (2 min)

```bash
cd ~/projects/job-tracker
claude
```
Type `/` and confirm you see **tailor** and **status**. `CLAUDE.md` loads automatically.

**✔ Done when** both commands appear.

---

### Step 6: First supervised run (10 min)

Paste a real job description (the whole text) and press Enter. Claude will:

1. Read the JD and check the tracker for duplicates.
2. Pick the base resume and create `applications/<date>_<company>_<role>/`.
3. Score your base resume (ATS before).
4. Tweak bullets, Technical Skills and Projects only; layout stays locked.
5. Compile and lint until every bullet is one line and it's one page.
6. Re-score (ATS after) and write `changes.md` + `ats_report.md`.
7. Log the job as **Applied** in `tracker/applications.csv`.
8. Commit and push.

The first time, it may ask permission for commands; choose **"Yes, don't ask again"**.

Audit this first one:
- [ ] Open `applications/<folder>/resume.pdf`: one page, same layout, bullets on one line?
- [ ] Read `changes.md`: is every "After" true?
- [ ] Check the new row in `tracker/applications.csv` on GitHub (it shows as a table).

**✔ Done when** you'd confidently submit that PDF.

---

## Phase B: Every application (about 3 minutes)

| Do | How |
|---|---|
| 1. Start | `cd ~/projects/job-tracker && claude` (or `/clear` between jobs) |
| 2. Paste the JD | Just paste. Already logged as Applied once it finishes. |
| 3. Read the summary | Base, ATS before → after, changes, gaps |
| 4. Correct if needed | "use the network resume", "keep the load balancer project", "don't drop Kubernetes" |
| 5. Get the PDF | `applications/<folder>/resume.pdf`. If the summary says "compile in Overleaf", paste `resume.tex` into Overleaf instead. |
| 6. Submit | Upload the PDF to the job site. Nothing else to log. |

Just testing a JD without applying? Add **"just check"** to your message.

**Status updates** (any time):
```
/status Amazon got an OA
/status Cisco rejected
/status            ← pipeline summary + follow-ups due
```

---

## Phase C: Maintenance

- **New project or job:** edit the right files in `resumes/` (or paste updated Overleaf source),
  then `git commit -am "update resumes" && git push`. The next run uses it.
- **Change how Claude tailors:** edit `.claude/skills/tailor/SKILL.md` in plain English,
  e.g. "For network roles always keep the Scalable Load Balancer project."
- **Weekly:** `/status` to see follow-ups due.

---

## Where everything lives

```
resumes/                     your 5 masters (never edited by tailoring)
applications/<folder>/       jd.md · keywords.json · resume.tex · resume.pdf · changes.md · ats_report.md
tracker/applications.csv     the spreadsheet (opens in Excel / Google Sheets; GitHub shows a table)
logs/CHANGELOG.md            one line per application
.claude/skills/tailor/       the pipeline + bullet_guidelines.md
.claude/skills/status/       status updates + pipeline summary
scripts/                     ats_score · lint_bullets · build_resume · preview_build · tracker · new_application · doctor
```

## Troubleshooting

| Problem | Fix |
|---|---|
| "missing: fontawesome5 newtx ulem" | `sudo tlmgr install fontawesome5 newtx ulem`, or use Overleaf for the PDF |
| `python3` not found (Windows) | Reinstall Python with "Add to PATH", or tell Claude "use python instead of python3" |
| `git push` fails | Run `git push` yourself once to sign in, or `gh auth login` |
| Slash commands missing | Start `claude` from inside the `job-tracker` folder |
| LinkedIn URL won't load | Paste the JD text instead |
| Lint "couldn't locate bullet in PDF" | Usually a hyphenated word; check that line by eye |
| Wrong base picked | Say "use the <track> resume instead"; it redoes the run |

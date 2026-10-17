---
name: tailor
description: Tailor my resume to a job description and log the application. Picks the right base resume (AI, Data Science, Network or Software), scores it ATS-style before and after, tweaks only bullets, Technical Skills and Projects (layout locked, one-line STAR/XYZ bullets), compiles it, logs the job as Applied in tracker/applications.csv, and commits + pushes to GitHub. Use whenever I paste a job description or job URL, even without saying /tailor. Pasting a JD means I have applied.
argument-hint: "<job description text or URL>  [just check]"
---

# Tailor resume + log application

Input: $ARGUMENTS (or the job description I pasted in my message)

Run every step without asking me to confirm. **Pasting a JD means I applied**, so log it
as `Applied` automatically; never ask me for a second "I applied" message.
Only exception: if my message says "just check" or "don't log", skip Steps 9–10.

## Step 1: Read the job
- URL only → fetch it. Fetch fails (LinkedIn/Handshake login wall) → ask me to paste the text, stop.
- Extract: company, role title, req/job ID, location, work mode, season, source, URL, deadline,
  pay, sponsorship info. Leave unknowns blank; never guess IDs or salary.

## Step 2: Duplicate check
`python3 scripts/tracker.py exists --company "<company>" --req-id "<id>" --role "<role>"`
If it reports a duplicate: still tailor, but skip Step 9 and tell me in one line.

## Step 3: Pick the base resume (one track)
| Track | File | Use for |
|---|---|---|
| `ai` | `resumes/resume_ai.tex` | AI / ML / LLM / computer vision / research |
| `datascience` | `resumes/resume_datascience.tex` | data science / analyst / data engineering / BI |
| `network` | `resumes/resume_network.tex` | network / infrastructure / IT / systems / cloud ops |
| `software` | `resumes/resume_software.tex` | software / full-stack / backend / embedded |
Match on job title first, then required skills. Hybrid role → the side with more required keywords.
Then: `python3 scripts/new_application.py --track <track> --company "<company>" --role "<role>"`
It prints the new folder; call it `$APP`. Save the JD to `$APP/jd.md` with the extracted
fields as a header.

## Step 4: Keywords + baseline score
Write `$APP/keywords.json`:
```json
{"title": "<role title>",
 "required":  [{"term": "Python", "aliases": ["Python3"]}],
 "preferred": [{"term": "Kubernetes", "aliases": ["k8s"]}]}
```
Required = minimum/required qualifications; preferred = nice-to-have. Concrete, matchable
terms only (languages, tools, platforms, methods like "REST APIs", "unit testing"); no soft
skills. 8–20 required, 5–15 preferred, with common aliases.
`python3 scripts/ats_score.py --keywords $APP/keywords.json --resume resumes/resume_<track>.tex --json` → ATS_BEFORE.

## Step 5: Tailor `$APP/resume.tex` (layout locked, three kinds of tweaks)
Read `.Codex/skills/tailor/references/bullet_guidelines.md` first.
**The bank** = every bullet, project and skill in ALL files in `resumes/` (the four resumes
+ `projects_bank.tex`), including commented-out `% \resumeItem{...}` lines and blocks.

**Locked, never change:** preamble, header, Education, section order and headings, every
`\vspace`, macros, employer names, job titles and dates (exactly as in the base file), and
the number of Experience entries.

**Tweak 1: Bullets** (Experience + Projects)
- Each bullet: strong past-tense verb + what + tech + measurable result.
  Present tense only for a role dated "Present".
- **Line rule: ONE full line, or TWO full lines, never an orphan.** A bullet whose second
  line holds only a few words is a defect. Fix it by (1) cutting 1–2 words so it fits on
  one line (preferred), or (2) adding real bank content for the same employer/project
  (a number, tool, scope or result) until line 2 is at least 85% full. Never pad with filler.
- Character count is NOT a reliable fit test (a 130-char bullet can fit while a 128-char
  one wraps). Trust `lint_bullets.py`, which measures rendered width.
- Most JD-relevant bullet first in each entry.
- Swap in a bank bullet for the same employer/project when it fits better.
- Reword to the JD's vocabulary only when it describes the same real work.
- Remove a bullet by commenting it out with `% ` (and its paired `\vspace` line).
- 2–4 bullets per Experience entry, 3–4 per project.
- Don't leave gaps when information is missing from one file: build a bullet from the bank
  that is factually correct for that Project/Experience. Don't leave the bottom of the page
  empty; fill it with relevant bank content. Use all the space available.

**Tweak 2: Technical Skills**
- Same number of lines, same LaTeX format; each line must fit on one line.
- Reorder lines and items so JD-required skills come first; you may rename a category
  and move items between lines.
- Add a skill ONLY if it appears somewhere in my `resumes/` files. Drop items irrelevant to the JD.

**Tweak 3: Projects**
- Same number of projects as the base file.
- Swap a less relevant project for a better one from any file, copying the whole
  `\resumeSubheading ... \resumeItemListEnd` block in the base file's format.
- Order projects chronologically, latest first and oldest at the bottom.
- Reorder each heading's tech list to lead with JD keywords, using only tech already
  listed for that project or named in its bullets.

**Never:** add a skill, tool, number, employer, title or date not in my files (report
missing required skills as Gaps; an honest 72 beats a fabricated 95) · estimate numbers ·
keyword-stuff. When files disagree on a fact, use the base file's version and list it under
"Fix in your files".
LaTeX: escape `& % $ # _` as `\& \% \$ \# \_`; "~30%" → `$\sim$30\%`.
Record every change as you go (before, after, why, rule) for Step 8.

## Step 6: Compile + lint until clean (max 5 rounds)
```
python3 scripts/build_resume.py $APP/resume.tex
python3 scripts/lint_bullets.py <LINT TARGET printed by build> --pdf
```
- Build exit 1 → fix the LaTeX error. Exit 2 → comment out the least relevant bullet.
- "orphan 2nd line" → cut the number of characters the lint names (1–2 whole words):
  filler → redundant qualifier → long names → secondary clause; keep verb, tech, number.
  Only if no cut is possible without losing meaning, add real bank content to fill line 2.
- "tight fit" warning → trim one easy word if one exists; otherwise leave it.
- Banned opener / -ing verb / pronoun / opener used 3+ times / escaping → fix as stated.
- Missing-number warnings → fix only if my files have the number.
- **Before finishing, open the compiled PDF page image and look at every bullet.** If any
  bullet's last line is short, it is not done, whatever the lint says.
Never change margins, font size or spacing.

## Step 7: Re-score
Same as Step 4 on `$APP/resume.tex` → ATS_AFTER. If it dropped, recheck your edits.

## Step 8: Write records
- `$APP/changes.md`: table `| # | Section | Before | After | Why | Rule |` for every edited
  bullet, then "Skills changes", "Projects swapped", "Removed".
- `$APP/ats_report.md`: ATS before → after, base track, keywords added, Gaps, Fix in your files.
- Append to `logs/CHANGELOG.md`:
  `- <YYYY-MM-DD> · <Company> — <Role> · <track> · ATS <before>→<after> · <n> bullets edited · <APP>`

## Step 9: Log as Applied
```
python3 scripts/tracker.py add --company "..." --role "..." --req-id "..." --location "..." \
  --work-mode "..." --season "..." --source "..." --job-url "..." --deadline "..." \
  --resume-track <track> --ats-before N --ats-after N --folder "$APP" \
  --keywords-added "a; b; c" --sponsorship "..." --pay "..."
```
(Status defaults to Applied, date = today, follow-up = +14 days.)

## Step 10: Commit + push
```
git add "$APP" tracker/applications.csv logs/CHANGELOG.md
git commit -m "applied: <Company> — <Role> (<track>, ATS <before>→<after>)"
git push
```
Push fails → keep the local commit and tell me the fix in one line.

## Step 11: Reply in exactly this shape
```
✅ <Company> — <Role> · base: <track> · logged Applied (<APP-ID>, follow-up <date>)
ATS: <before> → <after> · required <x>/<y> · lint: <errors> errors, <warnings> warnings · no orphan lines
Changes: <3–6 one-line bullets>
Skills: <moved/added/removed>   Projects: <kept/swapped>
Gaps: <missing required skills or "none">
Fix in your files: <conflicts, only if any>
PDF: $APP/resume.pdf  (or: "compile $APP/resume.tex in Overleaf", if build used preview)
Commit: <short sha> pushed
```
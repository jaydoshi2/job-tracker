# Job Applications: Summer 2027

Pasting a job description = I applied. Run the `tailor` skill automatically: pick the base
resume, tweak bullets/skills/projects, compile, log as Applied, commit and push.

## Commands
- Paste a JD (or `/tailor <JD>`): full pipeline. Add "just check" to skip logging.
- `/status <company> <news>` · `/status`: update or review the pipeline.

## Layout
- `resumes/`: resume_ai.tex, resume_datascience.tex, resume_network.tex, resume_software.tex,
  projects_bank.tex. These are my masters: NEVER edit them during tailoring. Only change them
  when I explicitly ask to update a master resume.
- `applications/<date>_<company>_<role>/`: jd.md, keywords.json, resume.tex, resume.pdf,
  changes.md, ats_report.md
- `tracker/applications.csv`: only modify via `scripts/tracker.py`.
- `logs/CHANGELOG.md`: one line per application.

## Hard rules
- Never invent skills, numbers, titles, dates or employers. Only use what's in `resumes/`.
- Keep my layout. Only bullets, Technical Skills and Projects change.
- Every bullet one line; resume exactly one page; never shrink margins/fonts.
- Commit + push after every application or status change.

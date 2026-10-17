# Resume Bullet Guidelines

Read this before writing or editing any bullet. `scripts/lint_bullets.py` enforces the mechanical rules (marked 🔒); the rest needs your judgment.

---

## 1. The formula: STAR thinking, XYZ writing

STAR (Situation, Task, Action, Result) is how you **think** through an accomplishment.
A resume line has no room to narrate all four, so compress it:
Situation and Task become implied context, Action and Result carry the line.

Write every achievement bullet in this shape:

```
[Strong past-tense verb] + [what you built/changed] + [using what tech] + [measurable result]
```

That is Google's XYZ formula ("accomplished X, as measured by Y, by doing Z") in
a reader-friendly order. Two valid orders:

| Order | Pattern | Example |
|---|---|---|
| Action-first (default) | Verb + Z (how, with tech) + X/Y (result) | Built a Flask REST API serving 20k daily requests, cutting p95 latency 35% |
| Result-first (for big wins) | Verb + X/Y (result) + by Z (how) | Cut CI build time from 14 to 4 min by caching Docker layers in GitHub Actions |

**Planning a bullet from the experience bank (do this silently):**
- S: What was broken, slow, missing, or needed? (stays implied)
- T: What were *you* specifically asked to do? (stays implied)
- A: What did *you* do, with which tools? → the verb + tech
- R: What changed, and by how much? → the number

If you can't find an R, use **scope** instead: users served, data volume, requests/day,
team size, number of services, frequency, or who adopted it.

---

## 2. One line per bullet 🔒

- Every bullet must render on **exactly one line** in the PDF. A wrapped bullet with
  a lonely 2–3 word second line wastes vertical space and looks unpolished.
- Target length: about 120–128 characters of plain text for an 11pt Times Jake-style template
  (fewer for wider fonts). `preview_build.py` + `lint_bullets.py --pdf` measure the real wrap.
- If it wraps, cut in this order:
  1. Filler words (`successfully`, `various`, `in order to` → `to`).
  2. Redundant context ("for the company's internal team" → "for 12 engineers").
  3. Long tool names (shorten "Amazon Web Services" to "AWS").
  4. A secondary clause. Keep the verb, the tech, and the number.
- Never shrink the font, margins, or line spacing to make bullets fit.
- If one achievement genuinely needs two lines, it's two achievements: split it.

---

## 3. Strong action verbs (not adverbs)

Start every bullet with a **specific past-tense verb** 🔒 (present tense only for a role
you're currently in). Adverbs like "successfully" or "efficiently" are filler: the
number proves success, so delete the adverb 🔒.

**Use no opener more than twice on the page** 🔒. Pick the verb that names what you
actually did.

| What you did | Verbs |
|---|---|
| Built something new | Architected, Built, Designed, Engineered, Implemented, Prototyped, Launched, Shipped, Deployed, Developed* |
| Made it better | Optimized, Accelerated, Reduced, Cut, Streamlined, Refactored, Scaled, Hardened, Boosted, Improved* |
| Automated / connected | Automated, Scripted, Orchestrated, Containerized, Migrated, Integrated, Consolidated, Standardized |
| Analyzed / debugged | Analyzed, Benchmarked, Profiled, Diagnosed, Debugged, Modeled, Evaluated, Quantified, Forecasted, Identified |
| ML / research | Trained, Fine-tuned, Researched, Investigated, Validated, Published, Labeled, Curated |
| Data | Aggregated, Cleaned, Visualized, Queried, Indexed, Partitioned, Pipelined |
| Led / taught | Led, Spearheaded, Mentored, Coordinated, Drove, Owned, Organized, Taught, Presented, Recruited |
| Secured / tested | Secured, Tested, Monitored, Instrumented, Audited, Patched, Resolved |

\* "Developed", "Created", and "Improved" are acceptable but generic. Prefer a more
specific verb when one fits.

**Banned openers** 🔒 (they describe proximity to work, not your contribution):
Responsible for · Duties included · Tasked with · Helped · Assisted · Aided ·
Worked on · Participated in · Involved in · Was · Utilized · Handled

**Banned anywhere** 🔒: I, me, my, our (the subject is implied).

---

## 4. Numbers and honesty

- Put a number in at least ~70% of experience bullets 🔒 (warning, not error).
  Good numbers: %, time saved, latency, throughput, users, records, $ saved,
  test coverage, error rate, number of services/endpoints, rank or award.
- **Only use numbers that exist in the experience bank.** If the bank says
  "about 30%", write "~30%" (as `$\sim$30\%` in LaTeX) and be ready to explain how
  you measured it.
- Never inflate team results into personal ones. "Contributed to a 26% growth"
  is honest if that's the truth; "Grew X by 26%" is not if it was a team effort.
- Test for every bullet: *Could I talk about this for two minutes in an interview,
  and would my former manager agree with it?* If not, rewrite it or cut it.

---

## 5. Tailoring without stuffing

- Mirror the JD's vocabulary **only when it describes the same real work**:
  bank says "made an API", JD says "RESTful services" → "Built RESTful services…".
- Put JD keywords in the **"using what tech"** slot naturally. A keyword inside a
  real achievement is worth more to a human reader than a keyword in a list.
- Each keyword should appear once or twice on the page, not five times.
- Lead each role with its most JD-relevant bullet. Recruiters often read only
  the first bullet of each entry.
- Also, you can change the bullet points according to requriements dosen't necessary need to stick with 
  same bullet point and change the words. 
- Add and bullet points according to need

---

## 6. Bullet counts

| Entry | Bullets |
|---|---|
| Most relevant / recent role | 3–5 |
| Older or less relevant role | 2–3 |
| Each project | 1–3 |
| Education coursework / skills lines | Label-style lines (e.g. "Coursework: …") are exempt from verb rules |

---

## 7. LaTeX hygiene 🔒

| Character | Write it as | Why |
|---|---|---|
| `&` | `\&` | Bare `&` is a table-column separator → build fails |
| `%` | `\%` | Bare `%` starts a comment → rest of the line silently disappears |
| `#` | `\#` | Macro parameter → build fails |
| `_` | `\_` | Subscript → build fails outside math |
| `$` | `\$` | Starts math mode |
| `~` before a number | `$\sim$` | Bare `~` is a non-breaking space, so "~30%" prints as " 30%" |
| `>`, `<` | `$>$`, `$<$` | Can print as ¡ ¿ in some font encodings |
| ranges | `--` (en dash) | `2025--2026`, `10--20\%` |
| C#, C++, .NET | `C\#`, `C++`, `.NET` | `#` must be escaped |

---

## 8. Before → after examples

| Weak | Strong (one line) | What changed |
|---|---|---|
| Responsible for fixing bugs in the backend | Resolved 40+ backend bugs in Python, cutting weekly production incidents by 30\% | Verb, count, tech, result |
| Helped build a dashboard for the team | Built a React dashboard tracking 12 KPIs, replacing a 2-hour weekly manual report | Ownership verb, scope, time saved |
| Worked on machine learning model for predictions | Trained an XGBoost churn model on 500k records, reaching 0.87 AUC (up from 0.79) | Specific verb, data size, metric |
| Successfully improved website performance | Cut page load time from 3.1s to 1.2s by lazy-loading images and code-splitting | Adverb removed, before/after numbers |
| Participated in a hackathon team project | Led a 4-person team to 2nd place of 60 teams at a university hackathon with Flask + OpenCV | Leadership verb, rank, tech |

---

## 9. Change log format (required for every edited bullet)

Every bullet you change goes into `$APP/changes.md` with the reason and the rule:

```
| # | Section | Before | After | Why | Rule |
|---|---|---|---|---|---|
| 1 | Company A | Built a REST API... | Built RESTful services in Flask... | JD asks for "RESTful services" | Tailoring §5 |
| 2 | Projects | Worked on campus app | Built a React + Node.js app used by 600+ students | Banned opener, no metric | §3, §4 |
```

Also list bullets **removed** (and why) and **added from the bank**. This log is how
I audit that nothing was invented.

---

## Sources consulted
- Google XYZ formula (Laszlo Bock): resume.io/blog/xyz-resume-format, ocs.yale.edu/resources/writing-impactful-resume-bullets
- Compressing STAR into bullets: resumeworded.com/star-method-resume-key-advice, airesume.guru/blog/star-method-resume-bullets
- Action verbs and passive openers: jobscan.co/blog/powerful-verbs-that-will-make-your-resume-stand-out, ecs.osu.edu (Quick Tips for Writing Strong Resume Bullets)
- Bullet length and counts: harvardcvmaker.com/guides/harvard-resume-bullet-points, extern.com/post/resume-bullet-points-guide
- Honest company achievements: themuse.com (Legit Way to List Company Accomplishments)

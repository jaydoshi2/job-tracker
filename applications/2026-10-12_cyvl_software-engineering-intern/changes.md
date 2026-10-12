# Changes: Cyvl — Software Engineering Intern (base: software)

| # | Section | Before | After | Why | Rule |
|---|---|---|---|---|---|
| 1 | Cenovus | Collaborated with cross-functional engineering teams to validate system integrations, debug cross-domain connectivity defects, and support production deployments with minimal disruption. | Collaborated with cross-functional engineering teams to debug connectivity defects and support production deployments. | JD: collaboration + shipping to production; one line | §5, §2 |
| 2 | Cenovus | Analyzed SolarWinds NPM metrics to perform root-cause analysis on performance degradation, resolving issues before they escalated into production outages. | Diagnosed performance degradation via root-cause analysis of SolarWinds NPM metrics, resolving issues before production outages. | One line | §2 |
| 3 | Cenovus | Integrated server, VMware virtualized, and backup systems into stable hosting environments, ensuring high availability of applications supporting plant operations. | Integrated server, VMware virtualized, and backup systems into stable hosting, keeping plant applications highly available. | One line | §2 |
| 4 | Cleveland-Cliffs | Developed automated ETL pipelines to extract and transform live sensor data from a legacy OpenVMS Alpha system into SQL server, cutting manual extraction effort by 40% and enabling continuous plant monitoring. | Automated ETL pipelines moving live sensor data from legacy OpenVMS Alpha into SQL Server, cutting manual effort by 40%. | JD: SQL + real-world data; one line | §5, §2 |
| 5 | Cleveland-Cliffs | Engineered a threshold-based anomaly detection tool comparing live isotope gauge measurements against ordered plate specifications, automating real-time defect flagging via email alerts to mill operators, reducing defective steel plate escapes by 30%. | Engineered a threshold-based anomaly detector on live gauge data with real-time email alerts, cutting defective plate escapes 30%. | One line | §2 |
| 6 | Cleveland-Cliffs | Engineered VB.NET journaling microservices via GitHub version control, deploying releases to a clustered QMS application, restoring TCP/IP data flow between production PLCs and SQL server within seconds. | Shipped VB.NET journaling microservices via Git/GitHub to a clustered QMS app, restoring PLC-to-SQL data flow in seconds. | JD: backend services shipped to production; one line | §5, §2 |
| 7 | Cleveland-Cliffs | (new; commented-out in base) Increased engineering and business decision efficiency by 50% by developing Power BI dashboards integrated with SQL views and stored procedures… | Built SQL views and stored procedures feeding Power BI dashboards, accelerating engineering and business decisions by 50%. | Page fill; JD requires SQL | Fill |
| 8 | IT Support | Imaged and deployed 150+ Windows devices using CLI tools for BIOS updates, data backups, and software installation. | Deployed 150+ Windows devices via CLI tools for imaging, BIOS updates, data backups, and software installation. | "Imaged" is not a verb-bank opener | §3 |
| 9 | Research | Improved control accuracy by 60% by writing Python scripts to process and analyze flight-test data from 15+ hardware trials, identifying performance trends… | Improved control accuracy by 60% with Python scripts analyzing real-world flight-test data from 15+ hardware trials. | JD: Python + messy real-world data; moved to first; one line | §5, §2 |
| 10 | Research | Reduced target navigation error by 40% by designing, implementing, and iteratively tuning a custom PID-based autonomous flight controller… | Reduced navigation error by 40% by tuning a custom PID flight controller in a ROS2-Gazebo digital twin via simulation tests. | One line | §2 |
| 11 | AI Job Application Agent | Built a **Claude Code** agent with custom skills that tailors 4 LaTeX resume tracks to a job post from a single prompt. | Same text, bold removed to match base format | JD requires AI coding agents (Claude Code) | §5 |
| 12 | AI Job Application Agent | Wrote a **Python** ATS scorer… | Same text, bold removed | Python + testing | §5 |
| 13 | AI Job Application Agent | Automated one-page, one-line and Workday parse checks… | Unchanged (from bank) | Well-tested code / automation | §5 |
| 14 | AI Job Application Agent | (new) Cut each job application to about **2minutes**… | Cut each job application to about 2 minutes by automating resume edits, PDF builds and tracker updates end to end. | Page fill; fixed "2minutes" spacing | Fill |
| 15 | SportsSight | Fine-tuned YOLOv8 on Roboflow football dataset… | Fine-tuned YOLOv8 on a Roboflow football dataset, achieving 90% player and ball detection accuracy on test video clips. | JD nice-to-have: YOLO, Roboflow, object detection | §5 |
| 16 | SportsSight | Applied K-Means pixel clustering for automated team assignment by t-shirt color, improving segmentation accuracy to 75%. | Implemented K-Means pixel clustering to assign players to teams by t-shirt color, reaching 75% segmentation accuracy. | "Applied" not a verb-bank opener; segmentation keyword | §3 |
| 17 | SportsSight | (new) Generated real-time match analytics on ball possession and movement patterns… | Unchanged from bank | Page fill | Fill |
| 18 | DeepTruth | Won RocketHacks 2025 for developing scalable AI fact-checking product used by 1,000+ users over a 6-month period. | Won RocketHacks 2025 for a full-stack React and Python AI fact-checking product used by 1,000+ users over 6 months. | JD nice-to-have: hackathon + full-stack; React/Python from heading; moved to first | §5 |
| 19 | DeepTruth | Built Python ETL pipeline with automated validation checks, improving data ingestion accuracy across 9,500+ records. | Validated 9,500+ records through a Python ETL pipeline with automated checks, improving data ingestion accuracy. | "Built" used 3×; messy-data validation | §3, §5 |

## Skills changes
- Programming Languages → "Programming Languages & Frameworks": Python, SQL first; added TypeScript (resume.tex), React, Django, FastAPI (resume_ai.tex); dropped C, R.
- New "AI Coding & Developer Tools": Claude-Code (plugins, skills, hooks), Cursor (resume_ai.tex), Git, GitHub Actions, Linux CLI, VS Code, Jupyter; dropped MATLAB.
- "Databases & Cloud": PostgreSQL first; added Supabase (resume_ai.tex), EC2, Docker, Kubernetes; dropped Firebase.
- "Data & Visualization" → "Machine Learning & Vision": Computer Vision, PyTorch, YOLOv8, OpenCV, Fine-Tuning, Model Evaluation, LLM, Hugging Face.
- "Software Development" → "Software Development & Data": REST APIs, CI/CD, Code Reviews, Unit Testing, Agile/SCRUM, Data Cleaning, Pandas, NumPy; dropped System Design, DS&A, Power BI, Tableau, Excel, Matplotlib.

## Projects swapped
- Added **AI Job Application Agent** (projects_bank.tex, Oct 2026–Present): matches "comfort with AI coding agents (Claude Code)".
- Added **SportsSight Analytics** (resume.tex / ai / datascience, Aug–Dec 2025): YOLO, Roboflow, detection, segmentation.
- Kept **DeepTruth** (hackathon, full-stack, labeled data).
- Removed **SkillBridge Learning Platform** and **PulseChat Application** (less relevant).
- Order: Agent (Present) → SportsSight (Dec 2025) → DeepTruth (Mar 2025).

## Removed
- DeepTruth: CI/CD GitHub Actions and AWS Lambda/CloudWatch bullets (project capped at 3; GitHub Actions/AWS kept in skills).
- SkillBridge and PulseChat blocks.

## Page fill
- Final fill_pct 100.0%, 0.0 lines free, 3 bullets added (Agent, SportsSight, Cleveland-Cliffs).

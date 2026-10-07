# Changes: Sigma Computing — Software Engineering Intern (base: resume_software.tex)

| # | Section | Before | After | Why | Rule |
|---|---|---|---|---|---|
| 1 | Cenovus | Analyzed SolarWinds NPM metrics to perform root-cause analysis on performance degradation, … (wrapped) | Analyze SolarWinds NPM metrics for root-cause analysis of performance degradation, resolving issues before production outages. | One line; present tense ("Present" role); moved first (performance focus) | §2, §3 |
| 2 | Cenovus | Collaborated with cross-functional engineering teams to validate system integrations, debug … (wrapped) | Debug connectivity defects and validate system integrations with cross-functional teams ahead of production deployments. | One line; present tense | §2, §3 |
| 3 | Cleveland-Cliffs | Engineered VB.NET journaling microservices via GitHub version control, … within seconds. (wrapped) | Deployed VB.NET microservices to a clustered QMS app, restoring TCP/IP data flow between PLCs and SQL Server in seconds. | One line; production software deployment first for SWE role | §2, Tailoring §5 |
| 4 | Cleveland-Cliffs | Developed automated ETL pipelines to extract and transform live sensor data … continuous plant monitoring. (wrapped) | Built ETL pipelines pulling live sensor data from legacy OpenVMS Alpha into SQL Server, cutting manual extraction by 40%. | One line | §2 |
| 5 | Cleveland-Cliffs | Engineered a threshold-based anomaly detection tool comparing live isotope gauge measurements … by 30%. (wrapped) | Automated real-time defect flagging by comparing live gauge data against plate specs, reducing defective plate escapes by 30%. | One line | §2 |
| 6 | Research Asst. | Improved control accuracy by 60% by writing Python scripts to process and analyze flight-test data … (wrapped) | Improved control accuracy by 60% with Python scripts analyzing flight-test data from 15+ hardware trials to find failure patterns. | One line; moved first (Python + number) | §2 |
| 7 | Research Asst. | Reduced target navigation error by 40% by designing, implementing, and iteratively tuning a custom PID … (wrapped) | Reduced navigation error by 40% by tuning a PID flight controller with simulation-driven testing in a ROS2-Gazebo digital twin. | One line | §2 |
| 8 | Research Asst. | Developed ROS2-Gazebo simulation pipeline to validate PX4 control logic on a digital twin … | Scripted Linux CLI tools for data collection, system configuration, and test logging across hardware and simulation environments. | Swapped in bank bullet (same role); JD requires Operating Systems | Tweak 1 swap |
| 9 | DeepTruth | Fine-tuned DistilBERT on 9.5K+ labeled records, … (ML, less relevant) | Shipped the frontend on AWS Amplify and the backend on a GCP VM, then tested the application with 50+ end users. | Bank bullet (projects_bank DeepTruth); JD stresses UI + backend, user feedback | Tweak 1 swap |
| 10 | Scalable Load Balancer | Automated rsync and database export/restore pipelines, … | Scripted rsync and database export/restore pipelines, … | "Automated" used 3× on page | §3 |

## Reordered (unchanged text)
- DeepTruth: CI/CD second, ETL validation third, RocketHacks (1,000+ users) last; tech list leads with Python, React, MongoDB.
- SkillBridge: PostgreSQL 80% query-performance bullet first, then microservices response time, then JWT/OAuth REST security; tech list now Django, PostgreSQL, REST APIs, JWT, AWS, NLP (all named in its bullets/heading).

## Skills changes
- Programming Languages: Java, Python, JavaScript first (JD's examples); added TypeScript (from resumes/resume.tex).
- Software Development: Data Structures & Algorithms and Operating Systems first (OS from coursework line in resume_network.tex); added Documentation (from resume.tex skills line); merged Agile/SCRUM.
- "Data & Visualization" renamed to "Frameworks & Data Visualization": added React, Django, Spring Boot (all in bank); kept Power BI, Tableau, Excel (PivotTables, Charts), Pandas, NumPy; removed Matplotlib, VLOOKUP/IF.
- Databases & Cloud: added EC2 to AWS.
- Developer Tools: added GitHub Actions, Docker; "Linux Command Line" → "Linux CLI"; removed MATLAB.

## Projects swapped
- PulseChat Application (Jan–Aug 2024) → Scalable Load Balancer (Aug–Dec 2025, from resume_network.tex): shows backend scaling, rate limiting and performance under 500+ users, which match the JD's "backend scales to handle multiple customers" and "optimize the performance". Bullets used verbatim except "Automated" → "Scripted" (#10).
- Projects ordered newest to oldest: Load Balancer (2025) → DeepTruth (early 2025) → SkillBridge (2024).

## Removed
- Cenovus: "Integrated server, VMware virtualized, and backup systems …" (infra; space for one-line bullets).
- DeepTruth: "Fine-tuned DistilBERT …" and "Designed AWS Lambda and CloudWatch cron workflows …" (ML-specific).
- Research Asst.: "Developed ROS2-Gazebo simulation pipeline …" (replaced by #8).

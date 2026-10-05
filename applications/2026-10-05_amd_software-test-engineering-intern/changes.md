# Changes: AMD, Software Test Engineering Intern/Co-Op (base: software)

| # | Section | Before | After | Why | Rule |
|---|---|---|---|---|---|
| 1 | Cenovus | Collaborated with cross-functional engineering teams to validate system integrations, debug cross-domain connectivity defects, and support production deployments with minimal disruption. | Debugged connectivity defects and validated system integrations with cross-functional teams ahead of production deployments. | JD: debugging, driving defects to closure; one line | §2, §5 |
| 2 | Cenovus | Analyzed SolarWinds NPM metrics to perform root-cause analysis on performance degradation, resolving issues before they escalated into production outages. | Analyzed SolarWinds NPM metrics for root-cause analysis of performance degradation, resolving issues before production outages. | One line | §2 |
| 3 | Cleveland-Cliffs | Engineered a threshold-based anomaly detection tool comparing live isotope gauge measurements against ordered plate specifications, automating real-time defect flagging via email alerts ..., reducing defective steel plate escapes by 30%. | Automated real-time defect flagging by testing live gauge measurements against plate specs, reducing defective plate escapes by 30%. | QA framing of the same work; moved first | §2, §5 |
| 4 | Cleveland-Cliffs | Engineered VB.NET journaling microservices via GitHub version control, deploying releases to a clustered QMS application, restoring TCP/IP data flow ... within seconds. | Deployed VB.NET microservices to a clustered QMS app, restoring TCP/IP data flow between PLCs and SQL Server in seconds. | One line (wording from earlier network tailoring) | §2 |
| 5 | Cleveland-Cliffs | Developed automated ETL pipelines to extract and transform live sensor data ... cutting manual extraction effort by 40% and enabling continuous plant monitoring. | Built ETL pipelines pulling live sensor data from legacy OpenVMS Alpha into SQL Server, cutting manual extraction by 40%. | One line; moved last | §2 |
| 6 | IT Support | (not in base) | Imaged and configured 150+ Windows PCs using CLI tools for BIOS updates, data backups, and software installation. | Swapped in from resume.tex (same role); JD: PC configuration (software and hardware). "deployed devices" → "configured PCs" | Tweak 1, §5 |
| 7 | Research Asst. | Reduced target navigation error by 40% by designing, implementing, and iteratively tuning a custom PID-based autonomous flight controller ..., using simulation-driven testing to debug control behavior before hardware deployment. | Reduced navigation error by 40% by tuning a PID flight controller with simulation-driven testing in a ROS2-Gazebo digital twin. | One line; kept "testing" | §2 |
| 8 | Research Asst. | Improved control accuracy by 60% by writing Python scripts to process and analyze flight-test data from 15+ hardware trials, identifying performance trends and failure patterns ... | Improved control accuracy by 60% with Python scripts analyzing flight-test data from 15+ hardware trials to find failure patterns. | One line | §2 |
| 9 | Research Asst. | Developed ROS2-Gazebo simulation pipeline to validate PX4 control logic ... | Scripted Linux CLI tools for data collection, system configuration, and test logging across hardware and simulation environments. | Swapped in from resume.tex (same role, reworded from "Utilized"); JD: Linux, test logging | Tweak 1, §3 |
| 10 | Load Balancer (swapped in) | Architected a three-node LAMP network with primary, backup, and HAProxy servers, sustaining 500+ users with zero downtime. + bank: "Stress-tested system to handle 500+ concurrent users with zero service degradation." | Stress-tested a three-node LAMP cluster with HAProxy failover, sustaining 500+ concurrent users with zero downtime. | Merged base + bank bullet of same project; JD: performance and reliability testing | Tweak 1, §5 |
| 11 | Load Balancer | Automated rsync and database export/restore pipelines ... | Scripted rsync and database export/restore pipelines ... | "Automated" used 3× | §3 |
| 12 | DeepTruth | Bullet order: Fine-tuned, ETL, CI/CD, Lambda, Won | ETL validation, CI/CD, user testing, Won | Test/validation first | §5 |
| 13 | DeepTruth | (projects_bank) Deployed frontend via AWS Amplify (GoDaddy DNS) and backend on GCP VM; tested the application with 50+ users. | Tested the application with 50+ end users after deploying the frontend on AWS Amplify and the backend on a GCP VM. | Swapped in from bank (same project); JD: end-user testing | Tweak 1 |
| 14 | SkillBridge | Built NLP-based recommendation engine using TF-IDF and cosine similarity, achieving 95% prediction accuracy in testing. (resume.tex) | Validated an NLP recommendation engine using TF-IDF and cosine similarity, achieving 95% prediction accuracy in testing. | Swapped in for the Gemini agent bullet; validation framing | Tweak 1, §5 |

## Skills changes
- "Programming Languages" → "Programming & Scripting": added VB.NET (Cleveland-Cliffs bullets), Bash Scripting, Powershell Scripting (resume_network); dropped R.
- "Software Development" → "Software QA & Development": Unit Testing and CI/CD first; added Code Reviews, Documentation (resume.tex); dropped System Design.
- "Developer Tools" → "Operating Systems & Tools", moved to line 3: Windows, Linux Command Line, WSL, Windows PowerShell, GitHub Actions, Docker (resume.tex), VMware, Virtual Box (resume_network); dropped Jupyter, VS Code, MATLAB (MATLAB moved to line 5).
- "Data & Visualization" → "Databases & Reporting": databases + Power BI, Tableau, Excel (JD: databases and reporting tools).
- "Databases & Cloud" → "Cloud & Data": AWS (added EC2), GCP, Pandas, NumPy, Matplotlib, MATLAB; dropped Firebase.

## Projects swapped
- PulseChat Application → Scalable Load Balancer (resume_network block). Order: Load Balancer → DeepTruth → SkillBridge.
- DeepTruth heading: added GitHub Actions (named in its bullet), reordered.

## Removed
- Cenovus: VMware integration bullet (commented out)
- Research Asst.: ROS2-Gazebo simulation pipeline bullet (commented out)
- DeepTruth: Fine-tuned DistilBERT (commented out); Lambda/CloudWatch bullet (not used)
- SkillBridge: Gemini agent and JWT/OAuth bullets (not used)

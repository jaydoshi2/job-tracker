# Changes: Clay — Software Engineer Intern (base: software)

| # | Section | Before | After | Why | Rule |
|---|---|---|---|---|---|
| 1 | Cenovus | Collaborated with cross-functional engineering teams to validate system integrations, debug cross-domain connectivity defects, and support production deployments with minimal disruption. | Collaborate with cross-functional teams to validate system integrations, debug connectivity defects, and support deployments. | Wrapped to 2 lines; role is "Present", so present tense | §2, §3 |
| 2 | Cenovus | Analyzed SolarWinds NPM metrics to perform root-cause analysis on performance degradation, resolving issues before they escalated into production outages. | Analyze SolarWinds NPM metrics for root-cause analysis of performance degradation, resolving issues before production outages. | Wrapped; present tense | §2, §3 |
| 3 | Cenovus | Integrated server, VMware virtualized, and backup systems into stable hosting environments, ensuring high availability of applications supporting plant operations. | Integrate server, VMware, and backup systems into stable hosting environments, ensuring high availability for plant applications. | Wrapped; present tense | §2, §3 |
| 4 | Cleveland-Cliffs | Developed automated ETL pipelines to extract and transform live sensor data from a legacy OpenVMS Alpha system into SQL server, cutting manual extraction effort by 40\% and enabling continuous plant monitoring. | Automated ETL pipelines moving live sensor data from legacy OpenVMS into SQL Server, cutting manual extraction by 40\%. | Wrapped; "Developed" used 3x | §2, §3 |
| 5 | Cleveland-Cliffs | Engineered a threshold-based anomaly detection tool comparing live isotope gauge measurements ... reducing defective steel plate escapes by 30\%. | Engineered threshold-based anomaly detection with real-time email alerts to operators, reducing defective plate escapes by 30\%. | Wrapped | §2 |
| 6 | Cleveland-Cliffs | Engineered VB.NET journaling microservices via GitHub version control, deploying releases to a clustered QMS application, restoring TCP/IP data flow between production PLCs and SQL server within seconds. | Shipped VB.NET journaling microservices to a clustered QMS app via GitHub, restoring PLC-to-SQL TCP/IP data flow in seconds. | Wrapped; "Engineered" overused; JD says "ship" | §2, §3, §5 |
| 7 | Research Asst. | Improved control accuracy by 60\% by writing Python scripts to process and analyze flight-test data from 15+ hardware trials, identifying performance trends and failure patterns... | Improved control accuracy 60\% with Python scripts analyzing flight-test data from 15+ hardware trials to surface failure patterns. | Moved to first (Python is JD-required); wrapped | §5, §2 |
| 8 | Research Asst. | Reduced target navigation error by 40\% by designing, implementing, and iteratively tuning a custom PID-based autonomous flight controller in a ROS2-Gazebo digital twin, ... | Reduced target navigation error by 40\% by building and tuning a custom PID flight controller tested in a ROS2-Gazebo digital twin. | Wrapped to 2 lines | §2 |
| 9 | Research Asst. | Developed ROS2-Gazebo simulation pipeline ... | Engineered a ROS2-Gazebo simulation pipeline ... | "Developed" used 3x | §3 |
| 10 | DeepTruth | (order) Fine-tune, ETL, CI/CD, Lambda, RocketHacks | RocketHacks win first, then fine-tune, Lambda/CloudWatch, CI/CD, ETL | JD asks for hackathons + AI features; Lambda/CloudWatch in Clay stack | §5 |
| 11 | SkillBridge | (order) microservices, Gemini agent, PostgreSQL, JWT | Gemini AI agent first, then PostgreSQL, JWT/REST, microservices | JD: "built features with LLMs"; Aurora Postgres | §5 |

## Skills changes
- "Programming Languages" → "Languages & Frameworks": Python, JavaScript, SQL lead; added React, Django, FastAPI (from resume_ai.tex); dropped R.
- "Data & Visualization" line replaced by "AI & Machine Learning": LLM, RAG, Embeddings, Fine-Tuning, Transformer Models, NLP, LangChain, MCP, Agentic-AI Workflow, Hugging Face (all from resume_ai.tex / bank).
- Databases & Cloud: PostgreSQL first; AWS expanded to (Lambda, S3, EC2, CloudWatch).
- Software Development: REST APIs, System Design first.
- Developer Tools: added GitHub Actions, Docker, Claude Code; dropped MATLAB.
- Developer Tools: added Netlify at the user's explicit request (2026-10-18). It is not in any master resume.

## Projects swapped
- Removed PulseChat Application (Java/Spring Boot, least JD-relevant).
- Added PolicyRAG Document Intelligence (from resume_ai.tex): LLM + embeddings + FastAPI. Order is now newest → oldest: PolicyRAG (Dec 2025), DeepTruth (Jan 2025), SkillBridge (Aug 2024).
- Tech lists reordered: DeepTruth leads with Python, React, AWS; SkillBridge adds Gemini API (named in its bullet).

## Removed
- PulseChat's 3 bullets (project swapped out). No other bullets removed.

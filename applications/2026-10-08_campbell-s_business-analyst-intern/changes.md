# Changes: Campbell's — Business Analyst Intern (base: datascience)

| # | Section | Before | After | Why | Rule |
|---|---|---|---|---|---|
| 1 | Cenovus | (commented) Collaborated with infrastructure, OT, and process-control engineers to validate system integrations… | Collaborate with infrastructure, OT, and process-control engineers to validate system integrations and support production cutovers. | Cross-team collaboration + integration validation ≈ BA role; present tense for current role | §3, §5 |
| 2 | Cenovus | Monitored network and server health through SolarWinds NPM… | Monitor network and server health in SolarWinds NPM, flagging performance degradation before it escalates into outages. | Trimmed to one line; present tense | §2, §3 |
| 3 | Cenovus | Integrated server infrastructure, VMware… | (removed) | Least JD-relevant | §6 |
| 4 | Cleveland-Cliffs | Built Power BI semantic models on SQL Server views… (2 lines) | Built executive-ready Power BI dashboards on SQL Server views and stored procedures, accelerating business decisions by 50%. | JD: Power BI dashboards for stakeholders; bank bullet (resume_ai) | §5 |
| 5 | Cleveland-Cliffs | (part of #4) | Modeled Power BI table relationships in a star schema and validated report totals against source tables for data accuracy. | JD: data concepts, STTM, UAT-style validation; split long bullet | §2, §5 |
| 6 | Cleveland-Cliffs | Developed ETL pipelines to extract and engineer features… | Streamlined data ingestion via ETL pipelines from legacy OpenVMS Alpha into SQL Server, cutting manual extraction 40%. | JD: automation / data integration; one line | §2, §5 |
| 7 | Cleveland-Cliffs | Engineered a classification-based anomaly detection tool… | Automated real-time defect flagging with email alerts to mill operators, reducing defective steel plate escapes by 30%. | JD: workflow automation; bank wording (resume_software/Network) | §5 |
| 8 | IT Support | Imaged and deployed 150+ Windows devices… | Managed 200+ IT assets through inventory tracking, device deployment, secure decommissioning, and life-cycle documentation. | JD: documentation / process; bank bullet | §5 |
| 9 | Research | Improved control-logic accuracy by 60% by quantifying… (2 lines) | Improved control-logic accuracy by 60% by quantifying performance trends with Pandas, NumPy, and Matplotlib across 15+ trials. | One line; 15+ trials from bank | §2, §4 |
| 10 | Research | Reduced target navigation error by 40%… (2 lines) | Reduced target navigation error by 40% by analyzing setpoint and response curves in QGroundControl and PX4 Flight Review. | One line | §2 |
| 11 | Research | Developed ROS2-Gazebo simulation pipeline… | (removed) | Least JD-relevant; space | §6 |
| 12 | DeepTruth | Fine-tuned DistilBERT… (first) | Built Python ETL pipeline with automated validation checks… (first) | Reordered: data validation leads | §5 |
| 13 | DeepTruth | (new from bank) | Validated the app through user testing with 50+ users after deploying the frontend on AWS Amplify and backend on GCP. | JD: UAT; projects_bank.tex | §5 |
| 14 | DeepTruth | Won RocketHacks 2025… processed data of 1000+ users during 6 months. | Won RocketHacks 2025 for developing a scalable AI fact-checking product used by 1,000+ users over a 6-month period. | Grammar | §3 |
| 15 | SkillBridge | Built NLP-based recommendation engine… | Engineered an NLP recommendation engine… | Avoid 3rd "Built" opener | §3 |

## Skills changes
- Lines renamed/reordered: Data Analysis & Visualization (SQL, Power BI, Excel first) → Methods & Practices (Agile, SCRUM, Data Modeling, Documentation) → AI & Agentic Tools → Databases & Cloud (SQL Server, Azure first) → Programming & Tools.
- Added from bank: Excel (PivotTables, VLOOKUP, Charts) [resume_software], Agile Methodologies/SCRUM/Documentation [resume_software/resume.tex], RAG [resume_ai], SQL Server [base bullets], Data Cleaning/Schema Designing [resume.tex].
- Removed: C, React, Django, Firebase, Linux CLI, MATLAB, Computer Vision, RL, Distributed Training, MLOps, Deep Learning, etc.

## Projects swapped
- SportsSight Analytics → PolicyRAG Document Intelligence (resume_ai.tex), Dec 2025–Jan 2026. Order: newest → oldest.
- Tech lists reordered (SkillBridge leads with PostgreSQL; Gemini API added — named in its bullet).

## Removed
- Cenovus VMware/VNC bullet; IT imaging bullet; ROS2-Gazebo bullet; DeepTruth CI/CD and AWS Lambda bullets; SkillBridge JWT/OAuth bullet. All for space and relevance.

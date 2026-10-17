# Changes: Micron Technology — HVM Process Engineer Intern (base: datascience)

| # | Section | Before | After | Why | Rule |
|---|---|---|---|---|---|
| 1 | Education | (none) | Relevant Coursework: Statistics, Database Systems, Kalman Filtering, Operating Systems, Software Engineering | JD requires SPC/DOE understanding; Statistics + Kalman Filtering confirmed by you on 2026-10-14; others from commented line in resume_Network.tex | Your earlier confirmation (Education normally locked) |
| 2 | Cleveland-Cliffs title | Data Processing Engineer Intern | Process Controls Intern | Your explicit request, 2026-10-16 | Your request (titles normally locked) |
| 3 | Cenovus | (commented out in base) Collaborated with infrastructure, OT, and process-control engineers… | Collaborated with OT and process-control engineers to troubleshoot cross-domain issues and support production cutovers. | JD: partner with process owners/operations; one line | §5, §2 |
| 4 | Cenovus | (software variant) Analyzed SolarWinds NPM metrics to perform root-cause analysis… | Diagnosed performance degradation via root-cause analysis of SolarWinds NPM metrics, resolving issues before production outages. | JD: identify/troubleshoot issues, structured problem solving | §5 |
| 5 | Cenovus | Monitored network and server health through SolarWinds NPM, identifying performance degradation… | Monitored network and server health in SolarWinds NPM, flagging production infrastructure degradation early. | JD: monitor process performance; one line | §5, §2 |
| 6 | Cenovus | Integrated server infrastructure, VMware virtual environments, setting up VNC… | (removed) | Least relevant; replaced by root-cause bullet | — |
| 7 | Cleveland-Cliffs | Developed ETL pipelines to extract and engineer features from live sensor data… | Developed ETL pipelines collecting live sensor data from legacy OpenVMS Alpha into SQL Server, cutting manual effort 40%. | JD: data collection systems; one line | §5, §2 |
| 8 | Cleveland-Cliffs | Engineered a classification-based anomaly detection tool analyzing live gauge data… | Unchanged, moved to first | JD: defects / yield / excursions | §5 |
| 9 | Cleveland-Cliffs | Built Power BI semantic models on SQL Server views, defining table relationships in a star schema… | Modeled Power BI star schemas on SQL Server views, validating totals against source data to speed decisions by 50%. | JD: data warehousing, data-driven decisions; "Built" used 3× | §5, §3 |
| 10 | Cleveland-Cliffs | (new, resume.tex) Developed SQL stored procedures, cleaned and filtered production data in views… | Wrote SQL stored procedures to clean and filter production data in views for downstream Power BI reporting. | Page fill; JD: data cleansing, database querying | Fill |
| 11 | IT Support | Imaged and deployed 150+ Windows devices… | Deployed 150+ Windows devices via CLI tools for imaging, BIOS updates, data backups, and software installation. | Verb-bank opener | §3 |
| 12 | Research | Reduced target navigation error by 40% by systematically analyzing setpoint and response curves in QGroundControl and PX4 Flight Review… | Reduced navigation error by 40% by analyzing setpoint and response curves in PX4 Flight Review to tune PID gains. | One line | §2 |
| 13 | Research | (new) | Prototyped PID control designs in MATLAB, trialing gain settings for the PX4 drone flight controller. | Your explicit request, 2026-10-16 (MATLAB used to trial PID control); JD lists MATLAB | Your request |
| 14 | Research | Improved control-logic accuracy by 60% by quantifying tracking performance with Pandas, NumPy, and Matplotlib, computing error metrics such as RMSE and overshoot… | Improved control-logic accuracy by 60% by computing RMSE and overshoot across trials with Pandas, NumPy, and Matplotlib. | Statistical data analysis; one line | §2 |
| 15 | Research | Developed ROS2-Gazebo simulation pipeline… | (removed) | Least relevant to process engineering; made room for MATLAB bullet | — |
| 16 | SportsSight | Generated real-time match analytics… | Unchanged, moved to 2nd | Data analytics | §5 |
| 17 | SportsSight | Applied K-Means pixel clustering… | (removed) | Project held at 3 | — |
| 18 | DeepTruth-AI | Built Python ETL pipeline with automated validation checks… | Unchanged, moved to first | JD: data cleansing | §5 |
| 19 | DeepTruth-AI | Won RocketHacks 2025 for developing scalable AI fact-checking product which processed data of 1000+ users during  6 months. | Won RocketHacks 2025 for developing a scalable AI fact-checking product that processed data from 1,000+ users over 6 months. | Grammar/spacing fix | §2 |
| 20 | SkillBridge | Designed PostgreSQL schemas with fact and dimensional modeling… | Unchanged, moved to first | JD: data warehousing | §5 |

Also removed: DeepTruth CI/CD and AWS Lambda bullets, SkillBridge JWT/OAuth bullet (projects capped at 3).

## Skills changes
- "Programming Languages & Frameworks" → "Programming & Analysis Tools": Python, SQL, MATLAB (moved from Developer Tools), Java, R, C++, Excel (VLOOKUP, IF, PivotTables, Charts) (from resume_software.tex); dropped C, JavaScript, React, Django.
- "Data & Visualization" → "Data Analytics & Visualization": added Data Cleaning, Data Modeling (resume.tex).
- "Databases & Cloud" → "Databases & Data Systems": SQL Server, Stored Procedures, ETL Pipelines, PostgreSQL, MySQL, MongoDB, Schema Designing; dropped Firebase and cloud.
- "AI & Machine Learning": cut to Anomaly Detection, Supervised/Unsupervised Learning, Model Evaluation, Computer Vision, NLP; dropped LLM/MCP/LangChain/RL/MLOps etc.
- "Developer Tools" → "Process Control & Tools": PID Control, Root-Cause Analysis, PLCs, SolarWinds NPM, QGroundControl, Linux Command Line, Git.

## Projects swapped
- None. Kept SportsSight (Dec 2025), DeepTruth-AI (Mar 2025), SkillBridge (Dec 2024), already in date order; bullets and tech lists reordered toward data analytics.

## Page fill
- Final fill_pct 98.6%, 0.63 lines free, 1 bullet added (Cleveland-Cliffs SQL data cleaning). A 5th Cleveland-Cliffs bullet (VB.NET PLC data flow) was tried and removed: over the entry's max of 4 and past the bottom margin.

# Changes: Corning — Advanced Process Controls Intern (base: software)

| # | Section | Before | After | Why | Rule |
|---|---|---|---|---|---|
| 1 | Cenovus | Collaborated with cross-functional engineering teams to validate system integrations, debug cross-domain connectivity defects, and support production deployments... | Collaborated with OT and process-control engineers to validate system integrations and support production cutovers. | Swapped in resume_ai.tex wording (process-control engineers); one line | Bank, §2 |
| 2 | Cenovus | Analyzed SolarWinds NPM metrics to perform root-cause analysis on performance degradation... | Analyzed SolarWinds NPM metrics to perform root-cause analysis, resolving performance issues before production outages. | One line | §2 |
| 3 | Cenovus | Integrated server, VMware virtualized, and backup systems ... ensuring high availability ... | Integrated server, VMware virtualized, and backup systems into stable hosting environments supporting plant operations. | One line; manufacturing context | §2 |
| 4 | Cleveland-Cliffs | Engineered a threshold-based anomaly detection tool comparing live isotope gauge measurements ... 30%. | Engineered threshold-based anomaly detection comparing live gauge data to plate specs, cutting defective plate escapes 30%. | Moved first: JD fault detection / defect classification | §5 |
| 5 | Cleveland-Cliffs | Developed automated ETL pipelines ... enabling continuous plant monitoring (40%) | Built ETL pipelines moving live OpenVMS sensor data into SQL Server for process monitoring, cutting manual effort 40%. | JD "process monitoring"; one line | §5, §2 |
| 6 | Cleveland-Cliffs | (commented out) Power BI dashboards ... 50% | Increased engineering and business decision efficiency by 50% with Power BI dashboards on SQL views and stored procedures. | Restored: JD data visualization, stakeholder communication | §5 |
| 7 | Cleveland-Cliffs | Engineered VB.NET journaling microservices ... production PLCs and SQL server ... | Deployed VB.NET journaling microservices to a clustered QMS app, restoring TCP/IP data flow between PLCs and SQL Server. | One line | §2 |
| 8 | Research Asst. | Reduced target navigation error by 40% by designing, implementing, and iteratively tuning a custom PID-based ... | Reduced target navigation error by 40% by iteratively tuning PID gains against setpoint and response curves in QGroundControl. | JD PID / control performance; wording from resume_datascience.tex | Bank, §5 |
| 9 | Research Asst. | Developed ROS2-Gazebo simulation pipeline to validate PX4 control logic on a digital twin... | Developed a ROS2-Gazebo digital twin of the Holybro X500 drone to simulate and validate PX4 control logic before flights. | JD simulation; X500 per your note | §5 |
| 10 | Research Asst. | Improved control accuracy by 60% by writing Python scripts ... 15+ hardware trials ... | Improved control accuracy by 60% by quantifying RMSE and overshoot in Python (Pandas, NumPy) across 15+ flight trials. | JD control performance / statistics; RMSE + overshoot from resume_datascience.tex | Bank |
| 11 | Research Asst. | — | Designed and evaluated a PPO-based reinforcement learning model for autonomous drone target navigation in ROS2-Gazebo. | Added from resume.tex: ML + controls | Bank |
| 12 | DeepTruth | Designed AWS Lambda and CloudWatch cron workflows for scheduled Transformer retraining... | Scheduled Transformer retraining with AWS Lambda and CloudWatch cron workflows for ML lifecycle management. | "Designed" opener used 3x | §3 |
| 13 | SkillBridge | Built NLP-based recommendation engine ... 95% | Engineered NLP-based recommendation engine ... 95% | "Built" opener used 3x; swapped in from resume_ai.tex | §3, Bank |
| 14 | SkillBridge | Developed Gemini API-powered AI agent for auto-generating ... content creation effort. | Developed Gemini API-powered AI agent auto-generating video transcripts and MCQs, reducing manual content effort. | Tight fit | §2 |

## Skills changes
- Programming Languages: Python, MATLAB, SQL first (JD: Python, MATLAB).
- Software Development line → **Controls & Simulation**: PID Control, Digital Twin, ROS2, Gazebo, PX4, QGroundControl, Reinforcement Learning.
- New **Machine Learning** line (from resume_ai.tex): Supervised/Unsupervised Learning, Anomaly Detection, Computer Vision, NLP, Deep Learning, MLOps.
- Databases & Cloud + Developer Tools merged into **Databases & Tools**; added SQL Server; dropped Firebase, Jupyter, VS Code.

## Projects swapped
- PulseChat → SportsSight Analytics (ML: YOLOv8, K-Means). Order: SportsSight (Aug 2025) → DeepTruth (Jan 2025) → SkillBridge (Aug 2024).
- SkillBridge: microservices + JWT bullets replaced by the NLP 95% prediction bullet (resume_ai.tex).

## Coursework
Statistics, Kalman Filtering, Database Systems, Operating Systems, Software Engineering →
**Kalman Filtering, Probability and Statistics, Stochastic Processes, Linear Algebra, Multivariable Calculus, Artificial Intelligence**.
Why: JD asks for statistics, dynamic systems, optimization, ML. Kalman Filtering (state estimation) and Stochastic Processes fit controls; Linear Algebra and Multivariable Calculus underpin MPC/optimization; Artificial Intelligence covers ML.

## Removed
- DeepTruth CI/CD bullet; SkillBridge microservices + JWT bullets; PulseChat project (less relevant to controls/ML).

# Changes: DoorDash — Machine Learning Engineer Intern (base: resume_ai.tex)

| # | Section | Before | After | Why | Rule |
|---|---|---|---|---|---|
| 1 | SkillBridge | Built NLP-based recommendation engine using TF-IDF and cosine similarity, achieving 95% prediction accuracy in testing. | Built an NLP-based recommender system using TF-IDF and cosine similarity, achieving 95% prediction accuracy in testing. | JD lists "Recommender systems" / "RecSys"; same work | Tailoring §5 |
| 2 | DeepTruth | Designed AWS Lambda and CloudWatch cron workflows for scheduled Transformer retraining and ML lifecycle management. | Orchestrated scheduled Transformer retraining with AWS Lambda and CloudWatch cron jobs for ML lifecycle management. | "Designed" used 3× on page; moved up to 2nd bullet (model retraining > CI/CD for ML role) | §3 |
| 3 | Cenovus | Monitored network and server health through SolarWinds NPM, … before they escalated into larger outages. (wrapped) | Monitor network and server health in SolarWinds NPM, flagging performance degradation before it escalates into outages. | One line; present tense for a "Present" role | §2, §3 |
| 4 | Cenovus | Collaborated with infrastructure, OT, and process-control engineers … with minimal disruption. (wrapped) | Collaborate with infrastructure, OT, and process-control engineers to validate system integrations and support production cutovers. | One line; present tense; JD values team player | §2, §3 |
| 5 | Cleveland-Cliffs | Developed ETL pipelines to extract and engineer features from live sensor data … by 40%. (wrapped) | Engineered sensor-data features via ETL pipelines from legacy OpenVMS Alpha into SQL Server, cutting manual extraction 40%. | One line; feature engineering for ML; moved to 2nd | §2 |
| 6 | Cleveland-Cliffs | Translated production data into executive-ready Power BI dashboards … by 50%. (wrapped) | Translated production data into Power BI dashboards on SQL views and stored procedures, accelerating decisions by 50%. | One line | §2 |
| 7 | Research Asst. | Developed ROS2-Gazebo simulation pipeline to validate PX4 control logic on a digital twin … | Designed and evaluated a PPO-based reinforcement learning model for autonomous drone target navigation using ROS2-Gazebo. | Swapped in bank bullet (resumes/resume.tex); ML research is core to the JD | Tweak 1 swap |
| 8 | Research Asst. | Increased control logic accuracy by 60% by scripting Python analysis of flight-test data across 15+ hardware trials. | Improved control-logic accuracy by 60% by computing RMSE and overshoot in Pandas and NumPy across 15+ hardware trials. | Bank wording (RMSE/overshoot, Pandas, NumPy) shows analytical problem solving | §5 |

## Reordered (unchanged text)
- Cleveland-Cliffs: anomaly detection (classification model) moved to first bullet.
- Research Asst.: PPO RL → RMSE analysis → PID tuning (research first).
- PolicyRAG: FAISS indexing + cosine-similarity reranking moved to first bullet (JD: Ranking, Search).
- Project tech lists: SkillBridge leads with TF-IDF, NLP; PolicyRAG leads with Python, FAISS; SportsSight adds "Computer Vision" (from bank heading) and drops Matplotlib; DeepTruth drops React.

## Skills changes
- AI & ML line moved to the top; leads with Supervised/Unsupervised, Deep Learning, Computer Vision, NLP, Reinforcement Learning. Removed LangChain, MCP, Agentic-AI Workflow (not relevant to this JD).
- Programming line: Python, Java, C++ first (JD's systems languages); removed React.
- "Data & Visualization" renamed to "ML Libraries & Data": added PyTorch, Hugging Face, FAISS, OpenCV, YOLOv8 (all in bank); removed Tableau.
- Databases & Cloud: removed Supabase.
- Developer Tools: added GitHub Actions; removed Cursor, Anti-Gravity.

## Projects swapped
- None. Kept all 4 and reordered by relevance: SkillBridge (RecSys) → PolicyRAG (search/ranking) → SportsSight (CV) → DeepTruth (NLP/PyTorch).

## Removed
- Cenovus: "Integrated server infrastructure, VMware …" (infra, not ML; space for one-line bullets).
- Research Asst.: "Developed ROS2-Gazebo simulation pipeline …" (replaced by PPO RL bullet).

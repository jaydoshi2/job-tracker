# Changes: Amgen, Undergrad Intern – Machine Learning Engineer (base: ai)

| # | Section | Before | After | Why | Rule |
|---|---|---|---|---|---|
| 1 | DeepTruth | Designed AWS Lambda and CloudWatch cron workflows for scheduled Transformer retraining and ML lifecycle management. | Automated scheduled Transformer retraining and ML lifecycle management with AWS Lambda and CloudWatch cron workflows. (1st) | JD: automation of model training pipelines, MLOps | §5 |
| 2 | DeepTruth | (resume_network) Built Python ETL pipeline with automated validation checks, improving data ingestion accuracy across 9,500+ records. | Cleaned 9,500+ records with a Python ETL pipeline and automated validation checks, improving data ingestion accuracy. | Swapped in from same project in another file; JD: clean/prepare data, ingestion | Tweak 1, §5 |
| 3 | DeepTruth | Automated CI/CD deployment via GitHub Actions and GCP VMs, reducing manual release steps and improving consistency. | Streamlined model deployment with CI/CD via GitHub Actions and GCP VMs, reducing manual release steps. | JD: deployment pipelines; avoid 3rd "Automated" | §3, §5 |
| 4 | SkillBridge | Built NLP-based recommendation engine ... | Built an NLP recommendation engine ... | Grammar | §3 |
| 5 | SkillBridge | Schemas bullet (3rd) | (same text, moved 2nd) | JD: data warehouses / database modeling | §5 |
| 6 | SkillBridge | Developed Gemini API-powered AI agent for auto-generating ... | Developed a Gemini API-powered AI agent auto-generating ... (moved 3rd) | Less relevant | §5 |
| 7 | SportsSight | Bullets: YOLOv8, K-Means, optical flow, analytics | YOLOv8, K-Means, analytics | JD: data-driven insights; 3-bullet trim | §5 |
| 8 | PolicyRAG | ... extracting text and tables from PDFs using pdfplumber. | ... parsing unstructured PDF text and tables with pdfplumber. | JD: structured and unstructured data | §5 |
| 9 | Cenovus | Monitored network and server health through SolarWinds NPM, ... | Monitored network and server health in SolarWinds NPM, flagging performance degradation before it escalated into outages. (1st) | JD: monitoring production; one line | §2 |
| 10 | Cenovus | Collaborated with infrastructure, OT, and process-control engineers to validate system integrations, troubleshoot ..., and support production cutovers with minimal disruption. | Collaborated with infrastructure, OT, and process-control engineers to validate system integrations and support production cutovers. | One line | §2 |
| 11 | Cleveland-Cliffs | Developed ETL pipelines to extract and engineer features from live sensor data (legacy OpenVMS Alpha OS) into SQL server, automating data ingestion and reporting to reduce manual extraction effort by 40%. | Automated ETL ingestion and transformation of OpenVMS Alpha sensor data into SQL Server, cutting manual extraction by 40%. | JD: ingestion + transformation pipelines; one line | §2, §5 |
| 12 | Cleveland-Cliffs | Translated production data into executive-ready Power BI dashboards integrated with SQL views and stored procedures, accelerating engineering and business decisions by 50%. | Developed Power BI semantic models on SQL Server views in a star schema, validating totals and accelerating decisions by 50%. | resume_datascience wording (same work); JD: dashboards, warehouses | Tweak 1, §5 |
| 13 | Research Asst. | Increased control logic accuracy by 60% by scripting Python analysis of flight-test data across 15+ hardware trials. | Increased control accuracy by 60% via statistical analysis of RMSE and overshoot in Pandas across 15+ hardware trials. (1st) | RMSE/overshoot + Pandas from resume_datascience; JD: statistical techniques | Tweak 1, §5 |
| 14 | Research Asst. | Developed ROS2-Gazebo simulation pipeline ... | Designed and evaluated a PPO-based reinforcement learning model for autonomous drone target navigation using ROS2-Gazebo. | Swapped in from resume.tex (same role); ML | Tweak 1 |

## Skills changes
- Programming: Python, SQL, R first; dropped C.
- AI & ML: Supervised/Unsupervised Learning, Model Evaluation (resume_datascience), NLP, MLOps first; dropped Computer Vision, LangChain, MCP, Agentic-AI.
- Data & Visualization: added Data Cleaning, Data Modeling (resume.tex), Excel (resume_software).
- Databases & Cloud: added Microsoft Azure (resume_datascience), EC2 kept; dropped Firebase, Supabase.
- "Developer Tools" → "Developer Tools & ML Libraries": Git, GitHub Actions, PyTorch, TensorFlow (resume_datascience SportsSight), Hugging Face, Jupyter, Colab, Agile/SCRUM (resume_network); dropped Cursor, Anti-Gravity, Claude-Code, VS Code.

## Projects swapped
- None. Reordered: DeepTruth → SkillBridge → SportsSight → PolicyRAG.
- SportsSight heading: added TensorFlow (listed for this project in your current resume_datascience.tex).

## Removed
- DeepTruth: RocketHacks win (commented out; 4-bullet cap)
- SportsSight: optical flow bullet (commented out)
- Cenovus: VMware integration bullet (commented out)
- Research Asst.: ROS2-Gazebo simulation pipeline bullet (commented out)

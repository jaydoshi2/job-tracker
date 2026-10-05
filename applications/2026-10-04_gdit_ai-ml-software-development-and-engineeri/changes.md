# Changes: GDIT, AI/ML Software Development and Engineering Intern (base: ai)

| # | Section | Before | After | Why | Rule |
|---|---|---|---|---|---|
| 1 | MCP Chatbot (swapped in) | Developed a local LLM chat application integrating Ollama models with the Model Context Protocol to enable dynamic tool discovery and multi-step, agentic tool-calling conversations. | Developed a local LLM chat app integrating Ollama models with Model Context Protocol for agentic, multi-step tool calling. | JD: agentic solutions, LLM front-end management; one line | §2, Tweak 3 |
| 2 | MCP Chatbot | Designed a tool-calling loop supporting up to 10 iterations per query across 4 built-in MCP tool categories (...), extensible via an optional GitHub MCP server ... | Orchestrated a tool-calling loop of up to 10 iterations per query across 4 MCP tool categories, extensible via a GitHub MCP server. | One line | §2 |
| 3 | MCP Chatbot | Implemented GitHub OAuth authentication and session management alongside a Streamlit dashboard exposing 10 REST endpoints for chat, tool discovery, model switching, and server monitoring. | Implemented GitHub OAuth and 10 REST endpoints for chat, tool discovery, model switching, and server monitoring. | JD: APIs, monitoring, security; one line | §2, §5 |
| 4 | DeepTruth | (network resume) Built Python ETL pipeline with automated validation checks, improving data ingestion accuracy across 9,500+ records. | Cleaned 9,500+ records with a Python ETL pipeline and automated validation checks, improving data ingestion accuracy. | Swapped in from resume_network (same project), replacing CI/CD bullet; JD: data cleaning | Tweak 1, §5 |
| 5 | DeepTruth | Designed AWS Lambda and CloudWatch cron workflows for scheduled Transformer retraining and ML lifecycle management. | Automated scheduled Transformer retraining and ML lifecycle management with AWS Lambda and CloudWatch cron workflows. | JD: workflow automation, deployment | §5 |
| 6 | DeepTruth | Won RocketHacks 2025 for developing scalable AI fact-checking product which processed data of 1000+ users during  6 months. | Won RocketHacks 2025 for building a scalable AI fact-checking product that processed data from 1,000+ users over 6 months. | Grammar | §3 |
| 7 | SkillBridge | (software resume) Reduced response time to under 15 seconds by designing microservices architecture integrating varied technologies across features. | Reduced response time to under 15 seconds by designing a microservices architecture integrating varied technologies. | Swapped in from resume_software (same project); JD: microservice architecture | Tweak 1 |
| 8 | SkillBridge | Built NLP-based recommendation engine using TF-IDF ... | Built an NLP recommendation engine using TF-IDF ... (moved 2nd) | ML fundamentals | §5 |
| 9 | SkillBridge | Developed Gemini API-powered AI agent for auto-generating ... | Developed a Gemini API-powered AI agent auto-generating ... | Grammar | §3 |
| 10 | Cenovus | Monitored network and server health through SolarWinds NPM, ... | Monitored network and server health in SolarWinds NPM, flagging performance degradation before it escalated into outages. (1st) | JD: monitoring; one line | §2 |
| 11 | Cenovus | Collaborated with infrastructure, OT, and process-control engineers to validate system integrations, troubleshoot ..., and support production cutovers with minimal disruption. | Collaborated with infrastructure, OT, and process-control engineers to validate system integrations and support production cutovers. | One line | §2 |
| 12 | Cleveland-Cliffs | Anomaly detection bullet (2nd) | (same text, moved 1st) | JD: ML, detection | §5 |
| 13 | Cleveland-Cliffs | Developed ETL pipelines to extract and engineer features from live sensor data (legacy OpenVMS Alpha OS) into SQL server, automating data ingestion and reporting to reduce manual extraction effort by 40%. | Engineered sensor-data features via ETL pipelines from legacy OpenVMS Alpha into SQL Server, cutting manual extraction 40%. | JD: data transformation; one line | §2 |
| 14 | Cleveland-Cliffs | Translated production data into executive-ready Power BI dashboards integrated with SQL views and stored procedures, accelerating engineering and business decisions by 50%. | Cleaned and filtered production data in SQL views and stored procedures for Power BI, accelerating decisions by 50%. | resume.tex wording ("cleaned and filtered production data in views"), same work; JD: data cleaning | Tweak 1, §5 |
| 15 | Research Asst. | Developed ROS2-Gazebo simulation pipeline to validate PX4 control logic ... | Designed and evaluated a PPO-based reinforcement learning model for autonomous drone target navigation using ROS2-Gazebo. | Swapped in from resume.tex (same role); ML | Tweak 1 |
| 16 | Research Asst. | Increased control logic accuracy by 60% by scripting Python analysis of flight-test data across 15+ hardware trials. | Increased control accuracy by 60% via statistical analysis of RMSE and overshoot in Pandas across 15+ hardware trials. | RMSE/overshoot + Pandas from resume_datascience (same work); JD: statistical methods, EDA | Tweak 1, §5 |
| 17 | Research Asst. | Order: PID, sim, Python | RL, 60% analysis, PID 40% | ML first | §5 |

## Skills changes
- Programming moved to line 1: Python, SQL first; added Streamlit; dropped C, R.
- AI & ML: Supervised/Unsupervised Learning first; dropped Computer Vision, Reinforcement Learning (still in a bullet), moved Hugging Face to libraries.
- "Data & Visualization" → "Data & ML Libraries": PyTorch (DeepTruth), Hugging Face, Pandas, NumPy, Matplotlib, Data Cleaning (resume.tex), Power BI, Excel (resume_software). Dropped Tableau.
- Databases & Cloud: added FAISS; dropped Firebase.
- Developer Tools: added GitHub Actions, Docker (resume.tex); dropped Anti-Gravity, VS Code.

## Projects swapped
- SportsSight Analytics-AI → MCP Chatbot (projects_bank.tex), named "MCP Chatbot-AI".
- Order: PolicyRAG → MCP Chatbot → DeepTruth → SkillBridge.

## Removed
- DeepTruth: CI/CD via GitHub Actions bullet (commented out; 4-bullet cap)
- SkillBridge: PostgreSQL schemas bullet (commented out)
- Cenovus: VMware integration bullet (commented out; least relevant)
- Research Asst.: ROS2-Gazebo simulation pipeline bullet (commented out)

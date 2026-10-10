# Changes: Docusign — Software Engineer Intern (base: software)

| # | Section | Before | After | Why | Rule |
|---|---|---|---|---|---|
| 1 | Cenovus | Analyzed SolarWinds NPM metrics to perform root-cause analysis… (2 lines) | Analyze SolarWinds NPM metrics for root-cause analysis of performance degradation, resolving issues before outages. | JD: metrics/observability; moved first; one line; present tense (current role) | §2, §3, §5 |
| 2 | Cenovus | Collaborated with cross-functional engineering teams to validate system integrations, debug… (2 lines) | Collaborate with cross-functional engineering teams to validate system integrations and debug cross-domain connectivity defects. | JD: cross-functional, debugging; one line | §2, §5 |
| 3 | Cenovus | Integrated server, VMware virtualized, and backup systems… | (commented out) | Least JD-relevant; space | §6 |
| 4 | Cleveland-Cliffs | Developed automated ETL pipelines… (2 lines) | Automated ETL pipelines moving live sensor data from legacy OpenVMS Alpha to SQL Server, cutting manual extraction 40%. | JD: data pipelines; one line | §2, §5 |
| 5 | Cleveland-Cliffs | Engineered VB.NET journaling microservices via GitHub version control… (2 lines) | Engineered VB.NET microservices under Git version control, restoring TCP/IP data flow from PLCs to SQL Server in seconds. | JD: services + version control; moved up; one line | §2, §5 |
| 6 | Cleveland-Cliffs | Engineered a threshold-based anomaly detection tool… (2 lines) | Built a threshold-based anomaly detection tool flagging defects via real-time email alerts, reducing steel plate escapes by 30%. | One line; avoid 2nd "Engineered" | §2, §3 |
| 7 | Cleveland-Cliffs | (commented out in base) Increased engineering and business decision efficiency by 50% by developing Power BI dashboards… | Developed Power BI dashboards on SQL views and stored procedures to monitor production data, accelerating decisions by 50%. | JD: metrics + basic dashboards; restored from the base file's own commented line | §5 |
| 8 | Research | Improved control accuracy by 60% by writing Python scripts… (2 lines) | Improved control accuracy by 60% by writing Python scripts to analyze flight-test data from 15+ hardware trials for failure patterns. | JD: Python; moved first; one line | §2, §5 |
| 9 | Research | Reduced target navigation error by 40% by designing, implementing… (2 lines) | Reduced target navigation error by 40% by implementing and tuning a custom PID flight controller in a ROS2-Gazebo digital twin. | One line | §2 |
| 10 | Research | Developed ROS2-Gazebo simulation pipeline… | (commented out) | Overlaps #9; space | §6 |
| 11 | MCP Chatbot | Developed a local LLM chat application integrating Ollama… (2 lines, projects_bank) | Developed a local LLM chat app integrating Ollama models with Model Context Protocol for dynamic, agentic tool calling. | JD: AI agent framework; one line | §2, §5 |
| 12 | MCP Chatbot | Designed a tool-calling loop supporting up to 10 iterations… (2 lines) | Designed an AI agent tool-calling loop of up to 10 iterations per query across 4 MCP tool categories, extensible via GitHub MCP. | JD: AI agents; one line | §2, §5 |
| 13 | MCP Chatbot | Implemented GitHub OAuth authentication and session management alongside a Streamlit dashboard… (2 lines) | Implemented GitHub OAuth and a Streamlit dashboard exposing 10 REST endpoints for chat, tool discovery, and server monitoring. | JD: REST APIs, dashboards, monitoring; one line | §2, §5 |

DeepTruth: kept the Fine-tuned, CI/CD, Lambda/CloudWatch and RocketHacks bullets unchanged. PolicyRAG: all 3 bullets copied unchanged from resume_ai.tex.

## Skills changes
- Programming Languages: Python, Java, JavaScript first; added TypeScript (from resume.tex) for the JD's "TypeScript/JavaScript".
- Software Development: Data Structures & Algorithms, REST APIs, Unit Testing first; added Code Reviews (resume.tex); Agile/SCRUM merged.
- Replaced Data & Visualization with AI & Machine Learning: LLM, RAG, LangChain, MCP, Agentic-AI Workflow, NLP, PyTorch, Transformers, Fine-Tuning, Model Evaluation, Hugging Face (from resume_ai/resume.tex; PyTorch from the DeepTruth heading).
- Databases & Cloud became Cloud & DevOps: Microsoft Azure (resume_datascience/resume.tex), Kubernetes and Docker (resume_Network), AWS incl. EC2, GCP, GitHub Actions.
- Developer Tools became Databases & Tools: PostgreSQL, MongoDB, MySQL, Git, Jupyter, Power BI Dashboards, Pandas, NumPy, Linux CLI.
- Removed: Firebase, Tableau, Excel, MATLAB, VS Code.

## Projects swapped
- SkillBridge → PolicyRAG Document Intelligence (resume_ai.tex): document extraction, RAG, vector search; matches the JD's clause/extraction work.
- PulseChat → MCP Chatbot (projects_bank.tex): agentic tool calling and REST endpoints; matches the JD's AI agent framework work.
- Order is newest first: PolicyRAG (Dec 2025) → MCP Chatbot (Aug 2025) → DeepTruth (Jan 2025).

## Removed
- Cenovus VMware bullet, ROS2-Gazebo pipeline bullet (commented out), plus the SkillBridge and PulseChat projects, swapped out for relevance.

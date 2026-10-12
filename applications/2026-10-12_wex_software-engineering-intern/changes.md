# Changes: WEX — Software Engineering Intern (base: software)

| # | Section | Before | After | Why | Rule |
|---|---|---|---|---|---|
| 1 | Cenovus | Analyzed SolarWinds NPM metrics to perform root-cause analysis on performance degradation, resolving issues before they escalated into production outages. | Diagnosed performance degradation via root-cause analysis of SolarWinds NPM metrics, resolving issues before production outages. | JD wants troubleshooting/debugging; moved to first | Tailoring §5, §2 |
| 2 | Cenovus | Collaborated with cross-functional engineering teams to validate system integrations, debug cross-domain connectivity defects, and support production deployments with minimal disruption. | Debugged cross-domain connectivity defects with cross-functional teams, supporting low-disruption production deployments. | Lead with "debug" (JD); one line | §3, §2 |
| 3 | Cenovus | Integrated server, VMware virtualized, and backup systems into stable hosting environments, ensuring high availability of applications supporting plant operations. | Integrated server, VMware virtualized, and backup systems into stable hosting, keeping plant applications highly available. | Wrapped to 2 lines | §2 |
| 4 | Cleveland-Cliffs | Engineered VB.NET journaling microservices via GitHub version control, deploying releases to a clustered QMS application, restoring TCP/IP data flow between production PLCs and SQL server within seconds. | Shipped VB.NET journaling microservices via Git/GitHub to a clustered QMS app, restoring PLC-to-SQL data flow in seconds. | JD requires Git/GitHub; moved to first; one line | §5, §2 |
| 5 | Cleveland-Cliffs | Developed automated ETL pipelines to extract and transform live sensor data from a legacy OpenVMS Alpha system into SQL server, cutting manual extraction effort by 40% and enabling continuous plant monitoring. | Automated ETL pipelines moving live sensor data from legacy OpenVMS Alpha into SQL Server, cutting manual effort by 40%. | JD: automate engineering workflows; one line | §5, §2 |
| 6 | Cleveland-Cliffs | Engineered a threshold-based anomaly detection tool comparing live isotope gauge measurements against ordered plate specifications, automating real-time defect flagging via email alerts to mill operators, reducing defective steel plate escapes by 30%. | Engineered a threshold-based anomaly detector with real-time defect email alerts, reducing defective plate escapes by 30%. | One line | §2 |
| 7 | IT Support | Imaged and deployed 150+ Windows devices using CLI tools for BIOS updates, data backups, and software installation. | Deployed 150+ Windows devices via CLI tools for imaging, BIOS updates, data backups, and software installation. | "Imaged" is not a verb-bank opener | §3 |
| 8 | Research | Reduced target navigation error by 40% by designing, implementing, and iteratively tuning a custom PID-based autonomous flight controller in a ROS2-Gazebo digital twin, using simulation-driven testing to debug control behavior before hardware deployment. | Reduced navigation error by 40% by tuning a custom PID flight controller in a ROS2-Gazebo digital twin via simulation tests. | One line | §2 |
| 9 | Research | Improved control accuracy by 60% by writing Python scripts to process and analyze flight-test data from 15+ hardware trials, identifying performance trends and failure patterns that guided each iteration of the control logic. | Improved control accuracy by 60% with Python scripts analyzing flight-test data from 15+ hardware trials. | One line | §2 |
| 10 | MCP Chatbot | Developed a local LLM chat application integrating Ollama models with the Model Context Protocol to enable dynamic tool discovery and multi-step, agentic tool-calling conversations. | Built a local LLM chat app on Ollama and the Model Context Protocol (MCP), enabling dynamic tool discovery and tool calls. | JD: MCP servers; from projects_bank; one line | §5, §2 |
| 11 | MCP Chatbot | Designed a tool-calling loop supporting up to 10 iterations per query across 4 built-in MCP tool categories (calculator, notes, tasks, unit conversion), extensible via an optional GitHub MCP server for repository operations. | Designed an agentic loop running up to 10 tool-calling iterations per query across 4 MCP tool categories. | JD: agentic infrastructure; one line | §5, §2 |
| 12 | MCP Chatbot | Implemented GitHub OAuth authentication and session management alongside a Streamlit dashboard exposing 10 REST endpoints for chat, tool discovery, model switching, and server monitoring. | Secured 10 REST endpoints for chat, tool discovery, and monitoring with GitHub OAuth and session management. | JD: REST APIs + SDLC security | §5, §2 |
| 13 | MCP Chatbot | (new) | Extended the agent with an optional GitHub MCP server for repository operations and a Streamlit dashboard for model switching. | Page fill; split from bank bullets 2 and 3 of the same project | Fill §10 |
| 14 | DeepTruth | Automated CI/CD deployment via GitHub Actions and GCP VMs, reducing manual release steps and improving consistency. | Automated CI/CD deployment via GitHub Actions workflows to GCP VMs, reducing manual release steps for consistency. | JD: GitHub Actions workflows; moved to first | §5 |
| 15 | DeepTruth | Fine-tuned DistilBERT on 9.5K+ labeled records, enabling dual-model scoring with 70% Gemini and 30% BERT weighting. | Integrated the Gemini API with DistilBERT fine-tuned on 9.5K+ labeled records, enabling dual-model scoring at 70/30 weighting. | JD: LLM APIs / API integrations | §5 |
| 16 | PulseChat | Architected MongoDB persistence layer and containerized deployment via Docker Compose for scalable, reproducible builds. | Containerized Spring Boot and MongoDB services with Docker Compose, producing scalable, reproducible builds and deployments. | JD preferred: Docker; moved to first | §5 |

Order only: PulseChat "Deployed application on AWS EC2…" moved to 2nd.

## Skills changes
- Programming Languages: added Bash Scripting (resume_Network.tex) and TypeScript (resume.tex); dropped R.
- Software Development: added Code Reviews and Documentation (resume.tex); "Agile Methodologies, SCRUM" → "Agile/SCRUM"; dropped System Design (line wrapped).
- "Data & Visualization" → "GenAI & Agentic AI": MCP, LLM, LangChain, Agentic-AI Workflow, RAG, Gemini API, Cursor, Claude-Code (from resume_ai.tex).
- "Databases & Cloud" → "Cloud & DevOps": AWS (Lambda, S3, EC2, CloudWatch), Microsoft Azure, GCP, Docker, Kubernetes, GitHub Actions.
- "Developer Tools" → "Developer Tools & Databases": Git, GitHub, Linux CLI, Windows PowerShell, VS Code, PostgreSQL, MySQL, MongoDB; dropped Jupyter, MATLAB, Firebase, Pandas/NumPy/Matplotlib, Power BI, Tableau, Excel.

## Projects swapped
- Added **MCP Chatbot** (projects_bank.tex, Aug–Dec 2025): MCP + agentic tool calling is the core of this role.
- Removed **SkillBridge Learning Platform** (least relevant; its REST/OAuth/agent points are covered by MCP Chatbot).
- Order: MCP Chatbot (Dec 2025) → DeepTruth (Mar 2025) → PulseChat (Aug 2024). Tech lists reordered to lead with JD keywords.

## Removed
- DeepTruth: "Built Python ETL pipeline with automated validation checks…" and "Won RocketHacks 2025…" (project held at Min 3; less relevant than CI/CD, Lambda and the Gemini API).
- SkillBridge block (swapped out).

## Page fill
- Final fill_pct 98.9%, 0.52 lines free, 1 bullet added (MCP Chatbot).

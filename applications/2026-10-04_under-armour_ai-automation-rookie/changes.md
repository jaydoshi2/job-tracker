# Changes: Under Armour, AI Automation Rookie (base: ai)

| # | Section | Before | After | Why | Rule |
|---|---|---|---|---|---|
| 1 | MCP Chatbot (swapped in) | Developed a local LLM chat application integrating Ollama models with the Model Context Protocol to enable dynamic tool discovery and multi-step, agentic tool-calling conversations. | Developed a local LLM chat app integrating Ollama models with Model Context Protocol for agentic, multi-step tool calling. | Agentic AI automation; one line | §2, Tweak 3 |
| 2 | MCP Chatbot | Designed a tool-calling loop supporting up to 10 iterations per query across 4 built-in MCP tool categories (...), extensible via an optional GitHub MCP server for repository operations. | Orchestrated a tool-calling loop of up to 10 iterations per query across 4 MCP tool categories, extensible via a GitHub MCP server. | One line; verb variety | §2, §3 |
| 3 | MCP Chatbot | Implemented GitHub OAuth authentication and session management alongside a Streamlit dashboard exposing 10 REST endpoints for chat, tool discovery, model switching, and server monitoring. | Implemented GitHub OAuth and a Streamlit dashboard exposing 10 REST endpoints for chat, tool discovery, and model switching. | One line | §2 |
| 4 | SkillBridge | Developed Gemini API-powered AI agent for auto-generating video transcripts and MCQs, reducing manual content creation effort. (2nd) | Built a Gemini API-powered AI agent auto-generating video transcripts and MCQs, reducing manual content creation effort. (1st) | JD: "reduce manual effort" with AI; moved first | §5 |
| 5 | SkillBridge | Built NLP-based recommendation engine using TF-IDF and cosine similarity, ... | Engineered an NLP recommendation engine using TF-IDF and cosine similarity, ... | Verb variety | §3 |
| 6 | DeepTruth | Order: Fine-tuned, CI/CD, Lambda, Won | CI/CD, Lambda, Fine-tuned, Won | Automation first | §5 |
| 7 | DeepTruth | Designed AWS Lambda and CloudWatch cron workflows for scheduled Transformer retraining and ML lifecycle management. | Orchestrated scheduled Transformer retraining with AWS Lambda and CloudWatch cron workflows for ML lifecycle management. | "Designed" used 4x; workflow vocabulary | §3 |
| 8 | DeepTruth | Won RocketHacks 2025 for developing scalable AI fact-checking product which processed data of 1000+ users during  6 months. | Won RocketHacks 2025 for building a scalable AI fact-checking product that processed data from 1,000+ users over 6 months. | Grammar | §3 |
| 9 | Cenovus | Collaborated with infrastructure, OT, and process-control engineers to validate system integrations, troubleshoot cross-domain connectivity issues, and support production cutovers with minimal disruption. | Collaborated with infrastructure, OT, and process-control engineers to validate system integrations and support production cutovers. | One line; cross-functional collaboration | §2 |
| 10 | Cenovus | Monitored network and server health through SolarWinds NPM, ... larger outages. | Monitored network and server health in SolarWinds NPM, flagging performance degradation before it escalated into outages. | One line | §2 |
| 11 | Cenovus | Integrated server infrastructure, VMware virtual environments, ... for plant operations. | Integrated servers, VMware virtual environments, networking, and backup systems for reliable plant application availability. | One line | §2 |
| 12 | Cleveland-Cliffs | Developed ETL pipelines to extract and engineer features from live sensor data (legacy OpenVMS Alpha OS) into SQL server, automating data ingestion and reporting to reduce manual extraction effort by 40%. | Automated ETL of live sensor data from legacy OpenVMS Alpha into SQL Server, cutting manual extraction by 40%. | Automation-led; one line | §2, §5 |
| 13 | Cleveland-Cliffs | Translated production data into executive-ready Power BI dashboards integrated with SQL views and stored procedures, accelerating engineering and business decisions by 50%. | Visualized production data in Power BI dashboards on SQL views and stored procedures, accelerating decisions by 50%. | One line; JD "smarter decision-making" | §2 |
| 14 | Research Asst. | Developed ROS2-Gazebo simulation pipeline to validate PX4 control logic ... | Designed and evaluated a PPO-based reinforcement learning model for autonomous drone target navigation using ROS2-Gazebo. | Swapped in AI bullet from resume.tex (same role) | Tweak 1 |
| 15 | Research Asst. | Order: PID, sim, Python | RL, Python 60%, PID 40% | AI/Python first | §5 |

## Skills changes
- "AI & Machine Learning" → "AI & Automation", moved to line 1; LLM, RAG, Agentic-AI, MCP, LangChain lead. Dropped Computer Vision, Reinforcement Learning, Deep Learning; moved Hugging Face to tools.
- Programming: Python, SQL first; added Streamlit (projects); dropped C, R.
- "Developer Tools" → "AI Developer Tools", moved to line 3: Claude-Code, Cursor, Anti-Gravity first; added GitHub Actions (DeepTruth); dropped Google Colab, VS Code.
- Data & Visualization: Power BI first.
- Databases & Cloud: added FAISS (PolicyRAG); dropped Firebase.

## Projects swapped
- SportsSight Analytics-AI (computer vision) → MCP Chatbot (projects_bank.tex), named "MCP Chatbot-AI" to match the other headings.
- Order: PolicyRAG → MCP Chatbot → SkillBridge → DeepTruth. SkillBridge heading gained "Gemini API" (named in its bullet).

## Removed
- Research Asst.: "Developed ROS2-Gazebo simulation pipeline ..." (commented out)
- Projects: SportsSight block (not used; still in master)

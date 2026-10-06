# Changes: Kensho, Machine Learning Engineer - Summer Intern 2027 (base: ai)

| # | Section | Before | After | Why | Rule |
|---|---|---|---|---|---|
| 1 | MCP Chatbot (swapped in, 1st) | Developed a local LLM chat application integrating Ollama models with the Model Context Protocol to enable dynamic tool discovery and multi-step, agentic tool-calling conversations. | Developed a local LLM chat app integrating Ollama models with Model Context Protocol for agentic, multi-step tool calling. | JD: agentic systems, LLM tool use; one line | Tweak 3, §2 |
| 2 | MCP Chatbot | Designed a tool-calling loop supporting up to 10 iterations per query across 4 built-in MCP tool categories (...), extensible via an optional GitHub MCP server ... | Orchestrated a tool-calling loop of up to 10 iterations per query across 4 MCP tool categories, extensible via a GitHub MCP server. | JD: LLM orchestration | §2, §5 |
| 3 | MCP Chatbot | Implemented GitHub OAuth authentication and session management alongside a Streamlit dashboard exposing 10 REST endpoints for chat, tool discovery, model switching, and server monitoring. | Implemented GitHub OAuth and 10 REST endpoints for chat, tool discovery, model switching, and server monitoring. | One line | §2 |
| 4 | Web Memory Assistant (swapped in) | Architected a local-first browser memory system with a Manifest V3 extension and FastAPI backend to capture, summarize, and semantically index web pages for instant recall. | Architected a local-first browser memory system with a Manifest V3 extension and FastAPI backend for semantic page recall. | JD: memory management, semantic search; one line | Tweak 3, §2 |
| 5 | Web Memory Assistant | Built a text-chunking pipeline splitting captured pages (up to 12,000 characters) into 400-word segments with 50-word overlap, embedding each into 384-dimensional vectors indexed in Pinecone for semantic search. | Embedded 400-word chunks (50-word overlap) as 384-dimensional vectors in Pinecone, enabling semantic search over saved pages. | JD: information retrieval, context engineering; one line | §2, §5 |
| 6 | Web Memory Assistant | Reduced noisy captures and backend load by filtering low-value pages via a 100-word extension threshold and 50-word API threshold, while automating tagging through Groq-powered summarization. | Cut noisy captures with 100- and 50-word filter thresholds and automated page tagging through Groq-powered summarization. | One line | §2 |
| 7 | DeepTruth | Order: Fine-tuned, CI/CD, Lambda, Won | Fine-tuned, Lambda retraining, ETL validation, Won | PyTorch/Transformers first; ML lifecycle | §5 |
| 8 | DeepTruth | Designed AWS Lambda and CloudWatch cron workflows for scheduled Transformer retraining and ML lifecycle management. | Automated scheduled Transformer retraining and ML lifecycle management with AWS Lambda and CloudWatch cron workflows. | JD: ML pipelines | §5 |
| 9 | DeepTruth | (resume_network) Built Python ETL pipeline with automated validation checks, improving data ingestion accuracy across 9,500+ records. | Cleaned 9,500+ records with a Python ETL pipeline and automated validation checks, improving data ingestion accuracy. | Replaces CI/CD bullet; "modeling real data" | Tweak 1 |
| 10 | DeepTruth | Won RocketHacks 2025 for developing scalable AI fact-checking product which processed data of 1000+ users during  6 months. | Won RocketHacks 2025 for building a scalable AI fact-checking product that processed data from 1,000+ users over 6 months. | Grammar | §3 |
| 11 | Cenovus | Collaborated ... validate system integrations, troubleshoot cross-domain connectivity issues, and support production cutovers with minimal disruption. | Collaborated ... to validate system integrations and support production cutovers. | One line; cross-functional | §2 |
| 12 | Cenovus | Monitored network and server health through SolarWinds NPM, ... | Monitored network and server health in SolarWinds NPM, flagging performance degradation before it escalated into outages. | One line | §2 |
| 13 | Cleveland-Cliffs | Developed ETL pipelines to extract and engineer features from live sensor data (legacy OpenVMS Alpha OS) into SQL server, automating data ingestion and reporting to reduce manual extraction effort by 40%. | Engineered sensor-data features via ETL pipelines from legacy OpenVMS Alpha into SQL Server, cutting manual extraction 40%. | One line; moved 2nd behind classification model | §2, §5 |
| 14 | Cleveland-Cliffs | Translated production data into executive-ready Power BI dashboards integrated with SQL views and stored procedures, accelerating engineering and business decisions by 50%. | Translated production data into Power BI dashboards on SQL views and stored procedures, accelerating decisions by 50%. | One line | §2 |
| 15 | Research Asst. | Developed ROS2-Gazebo simulation pipeline ... | Designed and evaluated a PPO-based reinforcement learning model for autonomous drone target navigation using ROS2-Gazebo. (1st) | Swapped in from resume.tex; advanced ML methods | Tweak 1 |
| 16 | Research Asst. | Increased control logic accuracy by 60% by scripting Python analysis of flight-test data across 15+ hardware trials. | Increased control accuracy by 60% via statistical analysis of RMSE and overshoot in Pandas across 15+ hardware trials. | RMSE/Pandas from resume_datascience; JD: statistical knowledge, modeling real data | Tweak 1, §5 |

## Skills changes
- AI & ML moved to line 1: Agentic-AI, LLM, RAG, MCP, LangChain lead; dropped Supervised/Unsupervised, Computer Vision; Hugging Face moved to libraries.
- Programming: Python, FastAPI, Streamlit lead (JD prototyping stack); dropped C, R.
- "Data & Visualization" → "ML Libraries & Data": PyTorch, Hugging Face, Pandas, NumPy, Matplotlib, Jupyter Notebook; dropped Tableau.
- Databases & Cloud: added SQLite, Pinecone (Web Memory Assistant), FAISS (PolicyRAG); dropped MySQL, Firebase, Supabase.
- Developer Tools: Claude-Code first (JD lists Claude Code); added GitHub Actions, Docker (resume.tex); dropped Anti-Gravity, Jupyter (moved).

## Projects swapped
- SportsSight Analytics-AI → MCP Chatbot (projects_bank.tex)
- SkillBridge Learning Platform-AI → Web Memory Assistant (projects_bank.tex)
- Order: MCP Chatbot → PolicyRAG → Web Memory Assistant → DeepTruth

## Removed
- DeepTruth: CI/CD bullet (commented out)
- Cenovus: VMware integration bullet (commented out)
- Research Asst.: ROS2-Gazebo simulation pipeline bullet (commented out)

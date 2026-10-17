# Changes: Aeromet — Image Processing Engineer Intern (base: resume_ai.tex)

| # | Section | Before | After | Why | Rule |
|---|---|---|---|---|---|
| 1 | SportsSight | Fine-tuned YOLOv8 on Roboflow football dataset, achieving 90% player and ball detection accuracy on test video clips. | Fine-tuned YOLOv8 on a Roboflow football dataset to detect and track players and ball, reaching 90% detection accuracy. | JD: "detection and tracking"; tracking is in the bank (projects_bank: "detecting and tracking football players") | §5 |
| 2 | SportsSight | Implemented optical flow and perspective transformation to compute real-world player speed and distance in meters. | Implemented optical flow and perspective transformation in OpenCV to compute real-world player speed and distance in meters. | Moved up; OpenCV is in the project's tech list; image processing | §5 |
| 3 | SportsSight | Applied K-Means pixel clustering for automated team assignment by t-shirt color, improving segmentation accuracy to 75%. | Applied K-Means pixel clustering to segment players by t-shirt color for team assignment, raising segmentation accuracy to 75%. | JD: image decomposition / segmentation | §5 |
| 4 | SportsSight | Generated real-time match analytics ... to support data-driven sports insights. | Generated real-time match analytics on ball possession and movement patterns from processed video frames. | Image-processing framing, trimmed filler | §2, §5 |
| 5 | Load Balancer (swapped in) | (network resume) Architected a three-node LAMP network with primary, backup, and HAProxy servers, sustaining 500+ users with zero downtime. | Architected a three-node Linux LAMP system with primary, backup, and HAProxy servers, serving 500+ users with zero downtime. | JD: Linux OS (LAMP = Linux) | §5 |
| 6 | Load Balancer | (network resume) Engineered HAProxy routing and per-IP rate limiting, capping traffic at 200 req/sec... | Engineered HAProxy Layer 4/7 routing and per-IP rate limiting, capping traffic at 200 req/sec while blocking abusive bursts. | Merged Layer 4/7 detail from projects_bank | bank |
| 7 | Load Balancer | (network resume) Automated rsync and database export/restore pipelines, cutting recovery time to under 5 minutes. | ...pipelines between nodes, cutting recovery time to under 5 minutes. | Fill line | §2 |
| 8 | Load Balancer | (network resume) Implemented encrypted Tailscale mesh networking to eliminate public exposure and enforce authenticated node access. | Implemented encrypted Tailscale mesh networking between nodes to eliminate public exposure and enforce authenticated access. | Added from bank to fill page | fill |
| 9 | DeepTruth-AI | Automated CI/CD deployment via GitHub Actions and GCP VMs, reducing manual release steps and improving consistency. | ...reducing manual release steps across the software lifecycle. | JD: software lifecycle process | §5 |
| 10 | DeepTruth-AI | Won RocketHacks 2025 ... which processed data of 1000+ users during 6 months. | Won RocketHacks 2025 for developing a scalable AI fact-checking product used by 1,000+ users over a 6-month period. | Grammar; software-resume wording | §2 |
| 11 | Smart Obstacle Avoidance Vehicle (swapped in) | Developed embedded C++ software with ultrasonic sensors & servo motors for real-time obstacle detection and navigation. | Developed embedded C++ software reading ultrasonic sensors and driving servo motors for real-time obstacle detection. | JD: C++, detection | §5 |
| 12 | Smart Obstacle Avoidance Vehicle | Implemented speed & distance tracking via IR sensor + rotating grid plate, achieving 85% measurement accuracy. | Built speed and distance tracking with an IR sensor and rotating grid plate, achieving 85% measurement accuracy. | JD: tracking; avoids a 3rd "Implemented" | §3 |
| 13 | Smart Obstacle Avoidance Vehicle | Integrated Bluetooth controls, reducing command response latency by ~60%... | (same wording, `$\sim$` escape) | Number from bank | §7 |
| 14 | Smart Obstacle Avoidance Vehicle | Designed & tested modular architecture with L293D driver, ensuring reliable integration and smooth motor control. | Designed and tested a modular architecture with an L293D motor driver, ensuring reliable integration and smooth motor control. | Added from bank to fill page | fill |
| 15 | Cenovus | Monitored network and server health through SolarWinds NPM, identifying ... before they escalated into larger outages. (2 lines) | Monitor network and server health in SolarWinds NPM, flagging performance degradation before it escalates into outages. | One line; present tense for Present role | §2 |
| 16 | Cenovus | Integrated server infrastructure, VMware virtual environments, networking, and backup systems ... (2 lines) | Integrate server infrastructure, VMware virtual environments, and backup systems to keep plant applications available. | One line | §2 |
| 17 | Cenovus | Collaborated with infrastructure, OT, and process-control engineers ... (2 lines) | Collaborate with infrastructure, OT, and process-control engineers to validate system integrations and production cutovers. | One line | §2 |
| 18 | Cleveland-Cliffs | Engineered a classification-based anomaly detection tool analyzing live gauge data, reducing defective steel plate escapes by 30%. | Engineered a classification-based anomaly detection tool on live gauge sensor data, reducing defective plate escapes by 30%. | Moved first; JD: detection, sensor/signal data | §5 |
| 19 | Cleveland-Cliffs | Developed ETL pipelines to extract and engineer features from live sensor data ... (2 lines) | Developed ETL pipelines moving live sensor data from legacy OpenVMS Alpha into SQL Server, cutting manual effort by 40%. | One line | §2 |
| 20 | Cleveland-Cliffs | Translated production data into executive-ready Power BI dashboards ... | Shipped VB.NET journaling microservices to a clustered QMS app, restoring TCP/IP data flow from PLCs to SQL Server. | Swapped in from resume_software.tex (same employer): software delivery fits this JD better than BI | swap |
| 21 | IT Support | Managed 200+ IT assets through inventory tracking ... | Imaged and deployed 150+ Windows devices using CLI tools for BIOS updates, data backups, and software installation. | Uncommented bank bullet; JD: Windows OS | swap |
| 22 | Research Assistant | Increased control logic accuracy by 60% by scripting Python analysis of flight-test data across 15+ hardware trials. | Increased control accuracy by 60% by analyzing flight-test signals from 15+ hardware trials in Python, NumPy, and Matplotlib. | Moved first; JD: Python, signal processing; NumPy/Matplotlib from datascience version | §5 |
| 23 | Research Assistant | Prototyped PID control designs in MATLAB, trialing gain settings for the PX4 drone flight controller. | ...trialing gain parameters... | JD: MATLAB, parameter-estimation vocabulary | §5 |
| 24 | Research Assistant | Developed ROS2-Gazebo simulation pipeline ... | Scripted Linux CLI tools for data collection, system configuration, and test logging across hardware and simulation runs. | Swapped in from resume.tex (same employer; banned opener "Utilized" fixed). JD: Linux | §3, swap |

## Skills changes
- Line 1: added MATLAB, Bash Scripting (from other resumes); dropped R.
- Line 2 renamed "AI & Machine Learning" → "Computer Vision & ML": leads with Computer Vision, OpenCV, YOLO, PyTorch; dropped NLP, LLM, RAG, LangChain, MCP, Transformer Models, RL, MLOps, Agentic-AI, Hugging Face (not relevant, and needed to fit one line).
- Line 3: NumPy moved first.
- Line 4 renamed "Databases & Cloud" → "Containers, OS & Cloud": Docker, Kubernetes, Linux, Windows, VMware, AWS, GCP; dropped PostgreSQL, MySQL, MongoDB, Firebase, Supabase.
- Line 5: added GitHub Actions, Linux CLI, Windows PowerShell, WSL, ROS2, Gazebo; dropped Cursor, Anti-Gravity, Google Colab.

## Projects swapped
- PolicyRAG Document Intelligence → Cloud-Native Load Balancer System (Docker, Linux).
- SkillBridge Learning Platform → Smart Obstacle Avoidance Vehicle (C++, detection).
- Kept SportsSight Analytics (moved first) and DeepTruth-AI (added Linux to its tech list, from projects_bank).

## Removed
- Cleveland-Cliffs Power BI bullet (replaced, see #20).
- IT asset-management bullet (commented out).
- Research ROS2-Gazebo simulation-pipeline bullet (commented out; 4-bullet cap).

# Changes: Wing — GNC Software Engineering Intern (base: software)

| # | Section | Before | After | Why | Rule |
|---|---|---|---|---|---|
| 1 | Education | (none) | Relevant Coursework: Statistics, Kalman Filtering, Operating Systems, Database Systems, Software Engineering | JD requires statistics/ML/optimization coursework; Statistics + Kalman Filtering confirmed by you in chat 2026-10-14; other courses from commented line in resume_Network.tex. Format copied from that commented block. | Your explicit request (Education normally locked) |
| 2 | Cenovus | Analyzed SolarWinds NPM metrics to perform root-cause analysis… | Diagnosed performance degradation via root-cause analysis of SolarWinds NPM metrics, resolving issues before production outages. | One line | §2 |
| 3 | Cenovus | Collaborated with cross-functional engineering teams to validate system integrations, debug… | Collaborated with cross-functional engineering teams to debug connectivity defects and support production deployments. | JD: work across engineering teams; one line | §2, §5 |
| 4 | Cenovus | Integrated server, VMware virtualized, and backup systems into stable hosting environments… | Integrated server, VMware virtualized, and backup systems into stable hosting, keeping plant applications highly available. | One line | §2 |
| 5 | Cleveland-Cliffs | Engineered a threshold-based anomaly detection tool comparing live isotope gauge measurements… | Engineered a threshold-based anomaly detector on live gauge data with real-time email alerts, cutting defective plate escapes 30%. | Real-time sensor data analysis; moved to first; one line | §5, §2 |
| 6 | Cleveland-Cliffs | Developed automated ETL pipelines to extract and transform live sensor data… | Automated ETL pipelines moving live sensor data from legacy OpenVMS Alpha into SQL Server, cutting manual effort by 40%. | One line | §2 |
| 7 | IT Support | Imaged and deployed 150+ Windows devices… | Deployed 150+ Windows devices via CLI tools for imaging, BIOS updates, data backups, and software installation. | Verb-bank opener | §3 |
| 8 | Research | Reduced target navigation error by 40% by designing, implementing, and iteratively tuning a custom PID-based autonomous flight controller… | Reduced target navigation error by 40% by tuning a custom PID flight controller in a ROS2-Gazebo digital twin. | JD: flight control; one line | §5, §2 |
| 9 | Research | Improved control accuracy by 60% by writing Python scripts to process and analyze flight-test data from 15+ hardware trials… | Improved control accuracy by 60% by analyzing flight data from 15+ hardware trials in Python, computing RMSE and overshoot. | JD: analyze flight data; RMSE/overshoot from resume_datascience.tex | §5 |
| 10 | Research | Developed ROS2-Gazebo simulation pipeline to validate PX4 control logic on a digital twin… | Validated PX4 control logic in a ROS2-Gazebo simulation linking flight controller and simulator over MAVLink/UDP. | JD: validate in simulated environments; resume_Network.tex wording | §5 |
| 11 | Research | (new, resume.tex) | Designed and evaluated a PPO-based reinforcement learning model for autonomous drone target navigation using ROS2-Gazebo. | Page fill; motion planning / autonomy | Fill |
| 12 | Research | (new, resume.tex) Assembled and configured Holybro X500 drone hardware… | Built and configured Holybro X500 drone hardware, supporting PX4-based feedback data collection and analysis. | Page fill; real physical systems; verb-bank opener | Fill, §3 |
| 13 | SportsSight | Implemented optical flow and perspective transformation… | Unchanged, moved to first | Geometric vision closest to state estimation | §5 |
| 14 | SportsSight | Fine-tuned YOLOv8 on Roboflow football dataset… | Fine-tuned YOLOv8 on a Roboflow football dataset, achieving 90% player and ball detection accuracy on test video clips. | JD: computer vision | §5 |
| 15 | SportsSight | Applied K-Means pixel clustering for automated team assignment… | Automated team assignment by t-shirt color via K-Means pixel clustering, improving segmentation accuracy to 75%. | Verb-bank opener | §3 |
| 16 | Multi-Agent Robotics Sim | Engineered a high-fidelity simulation pipeline using Gazebo Harmonic… | Unchanged (projects_bank.tex) | JD: simulation, controller logic | §5 |
| 17 | Multi-Agent Robotics Sim | Optimized collision physics and dynamics… 95%+ parity… | Unchanged | Sim-to-real validation | §5 |
| 18 | Multi-Agent Robotics Sim | Implemented multi-user/multi-agent communication protocols, allowing for synchronized control… | Built multi-agent communication protocols, enabling synchronized control and real-time data feedback. | "Implemented" used 3× | §3 |
| 19 | Smart Obstacle Avoidance Vehicle | Developed embedded C++ software with ultrasonic sensors & servo motors… | Developed embedded C++ software with ultrasonic sensors and servo motors for real-time obstacle detection and navigation. | JD: C++, embedded software, navigation | §5 |
| 20 | Smart Obstacle Avoidance Vehicle | Implemented speed & distance tracking via IR sensor + rotating grid plate… | Implemented speed and distance tracking via IR sensor and rotating grid plate, achieving 85% measurement accuracy. | Sensor-based estimation | §5 |
| 21 | Smart Obstacle Avoidance Vehicle | Integrated Bluetooth controls, reducing command response latency by ~60%… | Integrated Bluetooth controls, reducing command response latency by $\sim$60% and enabling near real-time mobile operation. | Fixed bare "~" escaping | §7 |

## Skills changes
- Programming Languages: C++ and Python first; added Bash Scripting (resume_Network.tex), MATLAB (moved from Developer Tools); dropped JavaScript, R.
- "Software Development" line → "Robotics & Autonomy": ROS2, Gazebo, PX4, MAVLink, QGroundControl, Rviz2, PID Control, Embedded Systems, Arduino (all from your files).
- "Data & Visualization" → "AI & Computer Vision": Machine Learning, Reinforcement Learning, Computer Vision, OpenCV, YOLOv8, PyTorch, Deep Learning.
- "Databases & Cloud" → "Software Development": Data Structures & Algorithms, Algorithm Design (resume.tex), System Design, Unit Testing, Git, Linux CLI; dropped databases/cloud.
- "Developer Tools" → "Data Analysis & Tools": NumPy, Pandas, Matplotlib, Jupyter Notebook, VS Code, Docker; dropped Power BI, Tableau, Excel.

## Projects swapped
- Added **SportsSight Analytics** (Aug–Dec 2025), **Multi-Agent Robotics Simulation** and **Smart Obstacle Avoidance Vehicle** (projects_bank.tex).
- Removed **DeepTruth**, **SkillBridge**, **PulseChat** (web/NLP, not GNC).
- Order: SportsSight (only dated one) first, then the two undated bank projects, which show their links in the date slot as in projects_bank.tex. The Multi-Agent link (Google Drive) is relabelled "Project Link" instead of "Github Link".

## Removed
- Cleveland-Cliffs: VB.NET journaling microservices bullet (least relevant; entry at 2).

## Page fill
- Final fill_pct 98.6%, 0.63 lines free, 2 bullets added (Research: PPO RL, Holybro X500).

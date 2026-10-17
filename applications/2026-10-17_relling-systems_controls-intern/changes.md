# Changes: Relling Systems — Controls Intern (base: software)

| # | Section | Before | After | Why | Rule |
|---|---|---|---|---|---|
| 1 | Cenovus | Collaborated with cross-functional engineering teams to validate system integrations, debug cross-domain connectivity defects… | Collaborated with OT and process-control engineers to validate system integrations and support production cutovers. | JD: work under engineers, commissioning; "OT, process-control" wording from resume_ai/network | §5, §2 |
| 2 | Cenovus | Analyzed SolarWinds NPM metrics to perform root-cause analysis… | Diagnosed performance degradation via root-cause analysis of SolarWinds NPM metrics, resolving issues before production outages. | JD: reproduce faults; one line | §5, §2 |
| 3 | Cenovus | Integrated server, VMware virtualized, and backup systems into stable hosting environments… | Integrated server, VMware virtualized, and backup systems into stable hosting, keeping plant applications highly available. | One line | §2 |
| 4 | Cleveland-Cliffs | Engineered a threshold-based anomaly detection tool comparing live isotope gauge measurements against ordered plate specifications… | Engineered a threshold-based anomaly detector comparing live gauge measurements to plate specs, cutting defective escapes 30%. | JD: record measurements; moved to first; one line | §5, §2 |
| 5 | Cleveland-Cliffs | Engineered VB.NET journaling microservices via GitHub version control… restoring TCP/IP data flow between production PLCs and SQL server within seconds. | Shipped VB.NET journaling microservices to a clustered QMS app, restoring PLC-to-SQL Server TCP/IP data flow. | PLC interface; "Engineered" used 3×; one line | §5, §3 |
| 6 | Cleveland-Cliffs | Developed automated ETL pipelines to extract and transform live sensor data… | Automated ETL pipelines moving live sensor data from legacy OpenVMS Alpha into SQL Server, cutting manual effort by 40%. | Sensor data; one line | §2 |
| 7 | IT Support | Imaged and deployed 150+ Windows devices… | Managed 200+ IT assets through inventory tracking, device deployment, secure decommissioning, and life-cycle documentation. | JD: documented results (bank bullet from resume_ai.tex / resume.tex) | §5 |
| 8 | Research | Reduced target navigation error by 40% by designing, implementing, and iteratively tuning a custom PID-based autonomous flight controller… | Reduced target navigation error by 40% by tuning a custom PID flight controller in a ROS2-Gazebo digital twin. | JD: control sequences; one line | §5, §2 |
| 9 | Research | Prototyped PID control designs in MATLAB… | Unchanged (from master, added 2026-10-16) | Controls testing | — |
| 10 | Research | Improved control accuracy by 60% by writing Python scripts to process and analyze flight-test data from 15+ hardware trials… | Improved control accuracy by 60% by analyzing flight-test data from 15+ hardware trials in Python to isolate failure patterns. | JD: record measurements, reproduce faults; one line | §5, §2 |
| 11 | Research | Developed ROS2-Gazebo simulation pipeline to validate PX4 control logic… | Validated PX4 control logic in a ROS2-Gazebo simulation linking flight controller and simulator over MAVLink/UDP. | JD: test procedures; resume_Network.tex wording | §5 |
| 12 | Smart Obstacle Avoidance Vehicle | Developed embedded C++ software with ultrasonic sensors & servo motors… | Developed embedded C++ software with ultrasonic sensors and servo motors for real-time obstacle detection and navigation. | JD: controls/electronics/robotics project, sensor interfaces | §5 |
| 13 | Smart Obstacle Avoidance Vehicle | Implemented speed & distance tracking via IR sensor + rotating grid plate… | Implemented speed and distance tracking via IR sensor and rotating grid plate, achieving 85% measurement accuracy. | Measurements | §5 |
| 14 | Smart Obstacle Avoidance Vehicle | Designed & tested modular architecture with L293D driver… | Designed and tested a modular L293D motor-driver architecture, ensuring reliable integration and smooth motor control. | "How you tested it" | §5 |
| 15 | Multi-Agent Robotics Sim | Engineered a high-fidelity simulation pipeline using Gazebo Harmonic… | Unchanged | Testing controller logic | §5 |
| 16 | Multi-Agent Robotics Sim | Optimized collision physics and dynamics for realistic interaction, ensuring 95%+ parity… | Optimized collision physics and dynamics, ensuring 95%+ parity between simulation and physical hardware. | Trimmed | §2 |
| 17 | Multi-Agent Robotics Sim | Implemented multi-user/multi-agent communication protocols… | Built multi-agent communication protocols, enabling synchronized control and real-time data feedback. | Verb variety | §3 |
| 18 | Automatic Street Light | Engineered an automatic light-dark sensing circuit using a 2N2222A transistor, LDR, and 1kΩ resistor… eliminating manual control entirely. | Designed an LDR light-sensing circuit with a 2N2222A transistor and 1kΩ resistor to switch an LED on ambient light. | JD: electronics project; "Engineered" used 3× | §5, §3 |
| 19 | Automatic Street Light | Soldered and assembled all components onto a physical circuit board, leveraging transistor base-voltage switching logic… | Built the circuit by soldering all components onto a physical board, eliminating manual light control entirely. | Split bank bullet (two achievements); verb-bank opener | Fill (split), §3 |
| 20 | Automatic Street Light | (split from bullet above) | Achieved fast-response, low-power operation under a 5V supply using transistor base-voltage switching logic. | Project min 3 bullets; facts from the same bank bullet | Fill (split) |

## Skills changes
- Programming Languages: C++, Python first; added MATLAB (from Developer Tools), Bash Scripting (resume_Network.tex); dropped JavaScript, R.
- "Software Development" → "Controls & Robotics": PID Control, PLCs, PX4, ROS2, Gazebo, MAVLink, QGroundControl, Rviz2, Simulation Testing.
- "Data & Visualization" → "Electronics & Embedded": Embedded Systems, Arduino, Circuit Design, Soldering, KiCad, Sensors, Motor Drivers, TinkerCAD (projects_bank.tex).
- "Databases & Cloud" → "Data & Analysis": Pandas, NumPy, Matplotlib, Root-Cause Analysis, SolarWinds NPM, SQL Server.
- Developer Tools: Git, Linux Command Line, VS Code, Jupyter Notebook, Docker.

## Projects swapped
- Added Smart Obstacle Avoidance Vehicle, Multi-Agent Robotics Simulation, Automatic Street Light (all projects_bank.tex). Removed DeepTruth, SkillBridge, PulseChat.
- None of the three has dates in your files, so they're ordered by relevance; right column shows their link / "Course Project" as in the bank.

## Removed
- Cenovus: none. Research: none (4 bullets). Cleveland-Cliffs Power BI bullet stays commented out.

## Page fill
- Final fill_pct 98.6%, 0.63 lines free; 1 bullet split to give the Street Light project its 3rd bullet.

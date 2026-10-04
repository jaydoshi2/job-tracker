# Changes: apexanalytix, IT & Cloud Intern (base: network)

| # | Section | Before | After | Why | Rule |
|---|---|---|---|---|---|
| 1 | Cenovus | Integrated server infrastructure, VMware virtual environments, networking, and backup systems to support reliable compute and application availability for plant operations. | Integrated servers, VMware virtual environments, networking, and backup systems for reliable plant application availability. | Moved to first (virtualization is JD's lead area); trimmed to one line | §2, §5 |
| 2 | Cenovus | Monitored network and server health through SolarWinds NPM, identifying performance degradation ... before they escalated into larger outages. | Monitored network and server health in SolarWinds NPM, flagging performance degradation before it escalated into outages. | JD health/performance monitoring; one line | §2 |
| 3 | Cenovus | Collaborated with infrastructure, OT, and process-control engineers to validate system integrations, troubleshoot cross-domain connectivity issues, and support production cutovers with minimal disruption. | Collaborated with infrastructure, OT, and process-control engineers to troubleshoot connectivity and support production cutovers. | One line; kept troubleshooting + teamwork | §2 |
| 4 | Cleveland-Cliffs | Developed automated ETL pipelines to extract and transform live sensor data from a legacy OpenVMS Alpha system into SQL server, cutting manual extraction effort by 40\% and enabling continuous plant monitoring. | Built ETL pipelines pulling live sensor data from legacy OpenVMS Alpha into SQL Server, cutting manual extraction by 40\%. | One line; stronger verb | §2, §3 |
| 5 | Cleveland-Cliffs | Engineered a threshold-based anomaly detection tool comparing live isotope gauge measurements ... via email alerts to mill operators, reducing defective steel plate escapes by 30\%. | Engineered real-time email alerts comparing isotope gauge data to plate specs, reducing defective steel plate escapes by 30\%. | Alerting = monitoring vocabulary; one line | §2, §5 |
| 6 | Cleveland-Cliffs | Engineered VB.NET journaling microservices via GitHub version control, deploying releases to a clustered QMS application, restoring TCP/IP data flow between production allen-bradley PLCs and SQL server within seconds. | Deployed VB.NET microservices to a clustered QMS app, restoring TCP/IP data flow between PLCs and SQL Server in seconds. | One line; avoid 3rd "Engineered" | §2, §3 |
| 7 | IT Support | (not present) | Imaged and deployed 150+ Windows devices using CLI tools for BIOS updates, data backups, and software installation. | Added from bank (resume.tex, same employer): firmware/BIOS updates + hardware maps to JD | Tweak 1 swap-in |
| 8 | Research Asst. | Improved control accuracy ... performance trends | (same) + period; moved first | Python scripting is JD-required | §5 |
| 9 | Research Asst. | Validated PX4 control logic by building a ROS2-Gazebo simulation ... MAVLink/UDP. | Scripted Linux CLI tools for data collection, system configuration, and test logging across hardware and simulation environments. | Swapped in bank bullet (resume.tex, same role; reworded from banned opener "Utilized"): Linux + logging | §3, Tweak 1 |
| 10 | Research Asst. | Reduced navigation error by 40\% ... DDS messaging | (same) + period; moved last | Less JD-relevant | §5 |
| 11 | Load Balancer | Architected a three-node LAMP network with primary, backup, and HAProxy servers, sustaining 500+ users with zero downtime. | Architected a high-availability three-node LAMP stack with HAProxy failover, sustaining 500+ users with zero downtime. | "high availability"/"failover" from bank version of same project; JD mentions HA clustering | §5 |
| 12 | Load Balancer | Automated rsync ... (4th) | moved to 2nd | Automation is JD-required | §5 |
| 13 | PulseChat | Architected MongoDB persistence layer and containerized deployment via Docker Compose for scalable, reproducible builds. | Containerized the Spring Boot and MongoDB stack with Docker Compose for scalable, reproducible builds and deployments. | Docker-first wording, moved first | §5 |
| 14 | PulseChat | Engineered real-time messaging platform ..., served 300+ university students. | Developed a real-time messaging platform ..., serving 300+ university students. | Grammar; verb variety (Engineered limit) | §3 |
| 15 | DeepTruth | Bullet order: Fine-tuned, ETL, CI/CD, Lambda, Won | CI/CD, Lambda, ETL, Won | Cloud/CI/CD first | §5 |

## Skills changes
- Line 1 "Networking & Systems Monitoring" → "Systems, Virtualization & Cloud" (moved first): Linux CLI, VMware, Virtual Box, Docker, Kubernetes, AWS (EC2, Lambda, S3, CloudWatch), GCP, Microsoft Azure. Added EC2/CloudWatch (from projects), Microsoft Azure (resume_datascience.tex). Dropped OpenVMs from skills (still in Cleveland-Cliffs bullet).
- "Programming Languages" → "Scripting & Automation": Bash and Python first; added GitHub Actions (CI/CD) (resume.tex / DeepTruth); dropped R.
- "Networking & Monitoring": TCP/IP, DNS, VLANs first (JD bonus list).
- Databases: added MariaDB (Load Balancer project); MySQL first.
- "Data & Visualization" → "Tools & Practices": added Git, WSL, Documentation, Agile/SCRUM (resume.tex / software); dropped Matplotlib.

## Projects swapped
- None swapped. Reordered: Scalable Load Balancer → PulseChat → DeepTruth (was DeepTruth first).
- Tech lists reordered; Linux added to Load Balancer heading (LAMP stack; bank version lists Linux).

## Removed
- Research Asst.: "Validated PX4 control logic ... MAVLink/UDP." (commented out; least infra-relevant)
- DeepTruth: "Fine-tuned DistilBERT ..." (commented out; ML, not infra; 4-bullet cap)

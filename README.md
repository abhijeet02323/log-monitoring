# Cloud Log Monitoring System

## Overview

Cloud Log Monitoring System is a Python-based security monitoring project built on Linux and AWS Cloud. The project collects and analyzes Linux system logs to detect suspicious activities such as failed SSH login attempts and invalid user access.

The system is designed to simulate real-world DevOps and cloud monitoring workflows by integrating Linux log analysis, Python automation, cloud infrastructure, Git version control, and database integration.

---

# Features

* Monitor Linux SSH logs using `journalctl`
* Detect failed login attempts
* Detect invalid SSH users
* Analyze system security events
* Real-time-ready project architecture
* AWS EC2 deployment support
* PostgreSQL database integration (upcoming)
* Docker support (upcoming)
* CI/CD integration with GitHub Actions (upcoming)

---

# Technologies Used

| Technology           | Purpose                     |
| -------------------- | --------------------------- |
| Python               | Log analysis and automation |
| Linux (Amazon Linux) | Server environment          |
| AWS EC2              | Cloud hosting               |
| Git & GitHub         | Version control             |
| PostgreSQL           | Log storage                 |
| Docker               | Containerization            |
| Flask                | Dashboard (future version)  |

---

# Project Architecture

```text
Linux System Logs
        ↓
journalctl
        ↓
Python Log Collector
        ↓
Filter Suspicious Logs
        ↓
Store Logs in Database
        ↓
Monitoring Dashboard
```

---

# Current Functionalities

The current version of the project:

* Reads SSH logs from Linux
* Filters failed login attempts
* Detects invalid users
* Displays suspicious activities in terminal

---

# Project Structure

```text
cloud-log-monitoring-system
│
├── collector
│   └── log_reader.py
│
├── database
│   └── schema.sql
│
├── dashboard
│
├── docker
│
├── requirements.txt
│
└── README.md
```

---

# Setup Instructions

## 1. Clone Repository

```bash
git clone https://github.com/yourusername/cloud-log-monitoring-system.git
```

---

## 2. Navigate to Project

```bash
cd cloud-log-monitoring-system
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Run the Log Monitoring Script

```bash
sudo python3 collector/log_reader.py
```

---

# Example Output

```text
Fetching system logs...

Detected Suspicious Activities:

Failed publickey for invalid user abhi from 192.168.x.x
Invalid user test from 192.168.x.x
```
---

# Why This Project?

This project was created to demonstrate practical implementation of:

* Linux system monitoring
* Cloud deployment
* Python automation
* DevOps concepts
* Security monitoring workflows

The goal is to build a real-world project suitable for DevOps and Cloud Engineering portfolios.

---
# Future Update Roadmap

## Version 1 — Current Development

* [x] Setup AWS EC2 Amazon Linux server
* [x] Configure Linux environment
* [x] Read Linux logs using `journalctl`
* [x] Build Python log collector
* [x] Detect failed SSH login attempts
* [x] Detect invalid SSH users
* [x] Filter suspicious logs
* [x] Create project structure
* [x] Configure GitHub repository
* [x] Create README documentation

---
# Future Improvements

* Real-time monitoring
* Email alerts
* Slack integration
* Flask dashboard
* Docker deployment
* Grafana visualization
* Prometheus integration
* CI/CD pipeline
* ELK Stack integration

---

# Learning Outcomes

Through this project, I learned:

* Linux logging systems
* SSH monitoring
* Python subprocess module
* AWS EC2 management
* Security log analysis
* DevOps workflow basics

---


# Cloud Log Monitoring System

> A Python-based Linux SSH log monitoring system that analyzes authentication logs to detect suspicious login activities. Built to demonstrate practical Linux administration, Python automation, cloud computing, and DevOps concepts through real-world implementation.

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Linux](https://img.shields.io/badge/Linux-Amazon%20Linux%20%7C%20Ubuntu-green)
![AWS](https://img.shields.io/badge/AWS-EC2-orange)
![Version](https://img.shields.io/badge/Version-v1.0-success)


---

# 📖 Overview

Cloud Log Monitoring System is a modular Python application that monitors Linux SSH authentication logs and identifies suspicious login activities such as:

* Failed password attempts
* Failed public-key authentication
* Invalid user access
* Authentication failures
* Unauthorized SSH connection events

The project is designed to simulate how security monitoring tools collect and process Linux system logs before forwarding them to monitoring platforms such as SIEM or SOC environments.

Rather than relying on third-party monitoring software, this project demonstrates the complete workflow using Python and native Linux logging utilities.

---

# ✨ Features

* Read Linux SSH logs using `journalctl`
* Detect suspicious authentication events
* Filter security-related log entries
* Modular Python architecture
* Sample log generator for testing
* Production mode using live Linux logs
* Ready for PostgreSQL integration (v1.1)

---

# 🏗 Project Architecture

```text
                    Linux Server
                (Amazon Linux / Ubuntu)
                          │
                          │
                    SSH Authentication
                          │
                          ▼
                  systemd-journald
                          │
                    journalctl -u sshd
                          │
        ┌─────────────────┴─────────────────┐
        │                                   │
        ▼                                   ▼
 Production Mode                     Sample Mode
 (Live Linux Logs)              sample_sshd.log
        │                                   │
        └──────────────┬────────────────────┘
                       ▼
               log_reader.py
                       ▼
               log_filter.py
                       ▼
          Suspicious Event Detection
                       ▼
              Console Output
                       ▼
         (Database Integration v1.1)
```

---

# ⚙️ Project Workflow

```text
SSH Authentication
        │
        ▼
Linux System Logs
        │
        ▼
journalctl
        │
        ▼
Python Log Reader
        │
        ▼
Log Filtering
        │
        ▼
Suspicious Event Detection
        │
        ▼
Display Security Events
```

---

# 🧩 Project Structure

```text
cloud-log-monitoring-system/
│
├── collector/
│   ├── log_reader.py
│   ├── log_filter.py
│   └── parser.py               # Upcoming (v1.1)
│
├── database/
│   ├── schema.sql
│   ├── db_connection.py        # Upcoming
│   └── insert_logs.py          # Upcoming
│
├── config/
│   └── config.py
│
├── logs/
│   ├── sample_sshd.log
│   ├── application.log
│   └── failed_logins.log
│
├── scripts/
│   └── generate_sample_logs.py
│
├── requirements.txt
├── main.py
└── README.md
```

---

# 🔍 How It Works

### Step 1 — SSH Activity

Every SSH login attempt (successful or failed) generates a system log.

Example:

```text
Failed password for root from 203.0.113.10 port 42420 ssh2
```

---

### Step 2 — Linux Logging

Linux stores authentication events using **systemd-journald**.

The application retrieves them using:

```bash
journalctl -u sshd
```

---

### Step 3 — Log Collection

`log_reader.py`

* Reads logs from Linux
* Or reads sample logs for testing
* Returns log entries to the application

---

### Step 4 — Log Filtering

`log_filter.py`

Filters only suspicious events such as:

* Failed password
* Failed publickey
* Invalid user
* Authentication failure

---

### Step 5 — Output

The filtered security events are displayed in the terminal.

Future versions will store these events inside PostgreSQL for analysis and dashboards.

---

# 🚀 Two Execution Modes

The project supports two modes.

## 1️⃣ Production Mode

Reads real SSH authentication logs directly from the operating system.

Source:

```bash
journalctl -u sshd
```

Recommended for:

* Linux servers
* AWS EC2
* Virtual Machines
* Local Linux installations

Configuration:

```python
LOG_SOURCE = "system"
```

---

## 2️⃣ Sample Mode

Reads predefined logs from

```text
logs/sample_sshd.log
```

Perfect for:

* Demonstrations
* Development
* Offline testing
* GitHub showcase

Configuration:

```python
LOG_SOURCE = "sample"
```

---

# 💻 Running Without AWS

AWS is **not required** to test this project.

Any Linux distribution using **systemd** can run it.

Examples:

* Ubuntu
* Debian
* Fedora
* CentOS Stream
* Rocky Linux
* AlmaLinux
* Arch Linux
* Amazon Linux

### Verify SSH logs are available

```bash
journalctl -u sshd
```

or on Ubuntu systems where the service may be named differently:

```bash
journalctl -u ssh
```

If logs are displayed, simply set:

```python
LOG_SOURCE = "system"
```

and run:

```bash
sudo python main.py
```

The application will read your local machine's SSH authentication logs exactly the same way it would on AWS EC2.

If you don't have SSH logs or simply want to test the application quickly, switch to:

```python
LOG_SOURCE = "sample"
```

and use the generated sample logs.

---

# 🛠 Technologies Used

| Technology       | Purpose                     |
| ---------------- | --------------------------- |
| Python           | Automation & log processing |
| Linux            | System log source           |
| systemd-journald | Linux logging service       |
| journalctl       | Retrieve SSH logs           |
| Git & GitHub     | Version control             |
| AWS EC2          | Production deployment       |
| PostgreSQL       | Database (v1.1)             |

---



# 🚨 Log Monitoring and Alerting System

A lightweight, Dockerized Python tool that scans system log files, detects warnings/errors, and prints alerts. Ideal for DevOps, automation, and learning basic monitoring principles.

---

## 🛠️ Features

- ✅ Parses `.log` files for `WARNING` and `ERROR` messages
- ✅ Displays alerts with timestamps
- ✅ Dockerized and portable
- ✅ Supports manual or scheduled (cron) log rotation
- ✅ Easy to deploy on GCP or any Linux server

---

## 📦 Run in Docker
```bash
    docker build -t logmonitor .
    docker run logmonitor
```

---
## Run this to rotate logs and generate a new one:

```bash
    chmod +x log-rotate.sh
    ./log-rotate.sh
```

## 🛠️ Tech Stack

| Technology / Tool        | Purpose                                                       |
|--------------------------|---------------------------------------------------------------|
| **Python 3**             | Parses log files, detects warnings/errors, and raises alerts |
| **Bash (Shell Scripting)** | Automates log generation and rotation tasks                 |
| **Docker / Podman**      | Containerizes the application for easy deployment            |
| **Google Cloud Platform (GCP)** | Runs the project in a free cloud environment via Cloud Shell |
| **Git & GitHub**         | Version control and collaboration                            |
| **Linux Commands**       | File handling, execution, and permission settings (`chmod`, `cat`, etc.) |

---

## 🔍 Key Concepts

- Log parsing & filtering
- Shell scripting
- Docker containerization
- Cloud deployment (GCP Shell)

## ☁️ Running on Google Cloud Shell (Free Tier)

This project was tested and executed on **Google Cloud Shell Editor**, a browser-based IDE provided by Google Cloud Platform. It offers a preconfigured development environment, built-in terminal, and requires no local setup.

### ✅ Why Google Cloud Shell?
- No setup required — runs in your browser
- Pre-installed tools like Python, Git, Docker
- Free usage with your Google account
- Persistent storage for your project files

### 🧪 How to Run
1. Go to [Google Cloud Shell](https://shell.cloud.google.com)
2. Clone the repository:
```bash
   git clone https://github.com/your-username/log-monitoring.git
   cd log-monitoring
```

## 🚀 Usage
To run the log monitoring script:
Run the log parser:

```bash
python3 log_parser.py
```

---
### 📷 Sample Output

This is how the log alert output looks when the script is executed:

![Log Monitoring Output](<img width="1917" height="853" alt="log-monitor-output" src="https://github.com/user-attachments/assets/4e511756-631a-4dcc-82f0-bfaf679c8da9" />
)

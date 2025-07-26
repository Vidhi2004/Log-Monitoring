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
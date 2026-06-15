# Python DevOps Automation Projects 🚀

A collection of real-world **Python automation scripts for DevOps, Linux, AWS, Docker, Monitoring, and Server Administration**.

This repository contains automation scripts built while learning **Python for DevOps Engineering** with a focus on solving practical infrastructure and operational tasks.

## Skills Covered

* Python Automation
* Linux Administration
* DevOps Engineering
* AWS Automation
* Docker Automation
* Monitoring & Alerting
* SSH Automation
* Backup Automation
* Security Auditing
* System Health Monitoring

---

# Project Structure

```txt
PYTHON-PRACTICE/
│── Advanced Linux Automation/
│   ├── auto_healing_service.py
│   ├── backup_scheduler.py
│   ├── cpu_alert.py
│   ├── disk_alert.py
│   ├── docker_auto_cleanup.py
│   ├── email_alert_system.py
│   ├── linux_security_audit.py
│   ├── log_monitor_with_alert.py
│   ├── memory_alert.py
│   ├── multi_server_health_checker.py
│   ├── server_inventory_generator.py
│   ├── slack_notification.py
│   ├── ssh_parallel_executor.py
│   └── website_auto_monitor.py
│
│── backups/
│
│── auto_patch_server.py
│── backup.py
│── calculator.py
│── conditionals.py
│── directory_size_checker.py
│── disk_cleanup.py
│── failed_login_detector.py
│── file_permission_checker.py
│── firewall_manager.py
│── fun_utils.py
│── hello.py
│── linux_user_creator.py
│── log_analyzer.py
│── loops.py
│── nginx_config_backup.py
│── old_log_cleaner.py
│── permission_changer.py
│── s3_backup.py
│── service_auto_restart.py
│── service_status_checker.py
│── ssh_automation.py
│── utils.py
│── website_monitor.py
│── README.md
│── requirements.txt
```

---

# Installation

Clone this repository:

```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/YOUR_REPOSITORY_NAME.git
```

Move into project directory:

```bash
cd YOUR_REPOSITORY_NAME
```

Install required dependencies:

```bash
pip install -r requirements.txt
```

---

# Requirements

Create a `requirements.txt` file:

```txt
boto3
paramiko
psutil
requests
schedule
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Linux Automation Scripts 🐧

### `service_auto_restart.py`

Automatically restarts failed Linux services.

### `service_status_checker.py`

Checks whether Linux services are running.

### `linux_user_creator.py`

Creates Linux users automatically.

### `file_permission_checker.py`

Checks file permissions.

### `permission_changer.py`

Changes Linux file permissions.

### `disk_cleanup.py`

Cleans temporary files from Linux systems.

### `old_log_cleaner.py`

Deletes logs older than a specified number of days.

### `log_analyzer.py`

Finds:

* ERROR
* WARNING
* FAILED

inside Linux log files.

### `failed_login_detector.py`

Detects failed SSH login attempts.

### `firewall_manager.py`

Manages Linux firewall rules using UFW.

### `directory_size_checker.py`

Checks large directory usage.

### `auto_patch_server.py`

Automatically updates Linux packages.

### `nginx_config_backup.py`

Backs up Nginx configuration.

---

# Advanced Linux Automation 🚀

### `multi_server_health_checker.py`

Checks multiple Linux servers through SSH.

Monitors:

* CPU
* RAM
* Disk
* Uptime

### `ssh_parallel_executor.py`

Runs commands on multiple servers simultaneously.

Useful for:

* health checks
* server maintenance
* infrastructure management

### `server_inventory_generator.py`

Creates CSV reports with:

* Hostname
* IP Address
* RAM
* Disk
* Uptime

### `linux_security_audit.py`

Performs Linux security checks:

* Open Ports
* Failed Login Attempts
* Sudo Users
* Suspicious Users

### `auto_healing_service.py`

Automatically restarts failed services.

### `backup_scheduler.py`

Creates scheduled backups automatically.

### `docker_auto_cleanup.py`

Automatically removes:

* stopped containers
* unused images
* unused volumes
* unused networks

### `website_auto_monitor.py`

Continuously monitors website availability.

### `log_monitor_with_alert.py`

Monitors logs in real-time and generates alerts.

### `cpu_alert.py`

Triggers alerts for high CPU usage.

### `disk_alert.py`

Checks disk usage and generates alerts.

### `memory_alert.py`

Checks RAM usage and generates alerts.

### `email_alert_system.py`

Sends automated email alerts.

### `slack_notification.py`

Sends Slack notifications using webhooks.

---

# AWS Automation ☁️

### `s3_backup.py`

Uploads backup files to AWS S3.

Features:

* S3 Upload
* Bucket Integration
* Backup Storage

### `backup.py`

Creates compressed backup files automatically.

---

# Monitoring & Alerts 📊

Scripts included:

* CPU Monitoring
* RAM Monitoring
* Disk Monitoring
* Website Monitoring
* Email Alerts
* Slack Alerts
* Log Monitoring

---

# Technologies Used

* Python
* Linux
* AWS S3
* Docker
* SSH
* DevOps Automation
* Monitoring
* System Administration

---

# How to Run

Run any script:

```bash
python3 filename.py
```

Example:

```bash
python3 docker_auto_cleanup.py
```

---

# Learning Goals

This repository is part of my DevOps learning journey.

The goal is to build hands-on automation projects related to:

* Linux
* AWS
* Docker
* Monitoring
* Infrastructure Automation
* Python for DevOps

---

# Future Projects

Planned additions:

* Kubernetes Automation
* Terraform Automation
* Jenkins Automation
* EC2 Automation
* EBS Snapshot Automation
* SSL Expiry Checker
* CI/CD Automation

---

# Connect With Me

LinkedIn: (https://www.linkedin.com/in/himanshugohil4)

GitHub: (https://github.com/himanshugohil18)

---

⭐ If you found this repository useful, feel free to star it.
# 🚨 Malicious IP Detection and Blocking System


## 📌 Problem Statement
Networks are under constant attack from known malicious IPs. This script automates the detection and blocking of those IPs using public threat feeds and system logs.

## 💡 Features
- Fetches IPs from AlienVault OTX
- Monitors logs in real-time (Linux/Windows)
- Blocks IPs via firewall rules
- Supports whitelist to avoid false positives
- SQLite-based alert logging

## 🧰 Tech Stack
- Python, watchdog, requests
- Linux IPTables / Windows Firewall
- AlienVault OTX

## 📦 Usage
1. Install dependencies: `pip install -r requirements.txt`
2. Add your AlienVault API key in `fetch_threat_feed.py`
3. Run `fetch_threat_feed.py` to update malicious IPs.
4. Run `log_monitor.py` to begin monitoring.

## ⚠️ Note
- Admin/root access is required for firewall modifications.
- Tested on Ubuntu 20.04 and Windows 10.

---
#   M a l i c i o u s _ I P _ D e t e c t i o n 
 
 

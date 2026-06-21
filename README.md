
# Cybersecurity Labs

This repository contains the cybersecurity projects I have built while learning Python and cybersecurity fundamentals. Rather than only reading about security concepts, I wanted to understand how they work by building simple tools myself.

These projects cover different areas of cybersecurity, including log analysis, network scanning, password security, and web application testing. As I learned more, I revisited several of these projects to improve them by adding features such as automated report generation, better error handling, and cleaner code.

---

# 📂 Projects

## 📄 [Log Parser](./Log-Parser/)

A Python script that analyzes server log files to identify failed login attempts. The program detects suspicious activity, counts failed logins, and generates a security report.

### Concepts Practiced
- Log Analysis
- File Handling
- Security Monitoring
- Basic Threat Detection

**Files**
- `log_parser.py`
- `server_logs.txt`
- `security_report.txt`

---

## 🌐 [Port Scanner](./Port-Scanner/)

A basic TCP port scanner built using Python's `socket` library. The scanner checks common ports on a target host, identifies open ports, and automatically generates a scan report.

### Concepts Practiced
- TCP/IP Networking
- Socket Programming
- Port Scanning
- Network Enumeration

**Files**
- `port_scanner.py`
- `port_scan_report.txt`

---

## 🔐 [Password Policy Auditor](./Password-Policy-Auditor/)

A password auditing tool that evaluates password strength based on length, character complexity, and a local breach dictionary. The program assigns a security score and provides recommendations for stronger passwords.

### Concepts Practiced
- Password Security
- Authentication
- Input Validation
- Security Policy Enforcement

**Files**
- `password_auditor.py`
- `common_breaches.txt`
- `password_audit_report.txt`

---

## 🌍 [Web Directory Scanner](./Web-Directory-Scanner/)

A simple web directory scanner that reads directory names from a custom wordlist and sends HTTP requests to determine whether those directories are accessible. The results are saved to a scan report.

### Concepts Practiced
- HTTP Requests
- Status Codes
- Web Enumeration
- Error Handling

**Files**
- `request_scanner.py`
- `wordlist.txt`
- `web_scan_report.txt`

---

# 🛠 Skills Demonstrated

- Python Programming
- File Handling
- Socket Programming
- HTTP Requests
- Network Fundamentals
- Log Analysis
- Password Security
- Basic Web Security
- Error Handling
- Report Generation

---

## About This Repository

These projects were built as part of my self-learning journey in cybersecurity. My goal is to strengthen my understanding of cybersecurity fundamentals through hands-on practice and continue expanding this repository with more advanced projects over time.
```

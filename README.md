# Cybersecurity-Labs

## 📂 Project 1: Linux Deployment & Automated Log Analysis Lab
* **Directory Path:** [`/Log-Parser-Lab`](./Log-Parser-Lab)
* **Core Technical Concept:** Security Monitoring & Log Analysis
* **Description:** Deployed a fully isolated virtual testing workstation using an Oracle VirtualBox Hypervisor to run a 64-bit Kali Linux kernel. Developed a custom automation utility in Python to scan high-volume server authentication files. The script dynamically maps security logs line-by-line, isolates brute-force attack signatures ("Failed login attempt"), cleans trailing data breaks using string manipulation, and surfaces the attacker's source IP addresses for defensive response.

---

## 📂 Project 2: Web Automation & Directory Vulnerability Scanner
* **Directory Path:** [`/Web-Scanner-Lab`](./Web-Scanner-Lab)
* **Core Technical Concept:** Network Automation & Vulnerability Auditing
* **Description:** Engineered an automated web infrastructure reconnaissance tool utilizing Python's `requests` engine to simulate sequential browser actions. The framework reads targeted dictionary paths from an input file (`wordlist.txt`) and handles network-level exceptions while transmitting sequential HTTP GET requests against remote web servers (`httpbin.org`). The tool tracks live server response codes, highlighting successful entries (Status 200) to expose unprotected or hidden directories left active on web platforms.

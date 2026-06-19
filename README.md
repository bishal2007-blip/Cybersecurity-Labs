# Cybersecurity-Labs

Welcome to my hands-on security engineering portfolio. This repository serves as a centralized, structured sandbox tracking my technical labs in defensive automation, infrastructure auditing, network recon, and identity assurance management.

Every lab was engineered inside an isolated VirtualBox testing environment running a 64-bit Kali Linux kernel, utilizing standalone Python scripts interacting with live network layers and data streams.

---

## 📂 Project 1: Linux Deployment & Automated Log Analysis Lab
* **Directory Path:** [`/Log-Parser-Lab`](./Log-Parser-Lab)
* **Core Technical Domain:** Security Information & Event Management (SIEM) / Log Parsing
* **Description:** Developed a custom automated parser to ingest and audit high-volume server authentication logs sequentially. The script targets and isolates signature brute-force attack indicators (`"Failed login attempt"`), processes raw strings to clean trailing structural breaks, and surfaces suspicious source IP addresses in real time for security operations response.
* **Key Files:** `log_parser.py` (Automation utility), `server_logs.txt` (Raw network log data).

---

## 📂 Project 2: Web Automation & Directory Vulnerability Scanner
* **Directory Path:** [`/Web-Scanner-Lab`](./Web-Scanner-Lab)
* **Core Technical Domain:** Application Security / Automated Reconnaissance
* **Description:** Engineered an automated directory mapping framework using Python's `requests` engine to simulate automated administrative discovery patterns. The tool reads targeted directory pathways from a dictionary wordlist (`wordlist.txt`), handles network-level connection exceptions, and maps live server HTTP status response codes (such as isolating successful `200 OK` hits) to reveal hidden web endpoints and exposed file assets.
* **Key Files:** `request_scanner.py` (Scanning script), `wordlist.txt` (Target pathways).

---

## 📂 Project 3: Network Transmission Port Scanner
* **Directory Path:** [`/Port-Scanner-Lab`](./Port-Scanner-Lab)
* **Core Technical Domain:** Network Layer Architecture / Vulnerability Assessment
* **Description:** Built a multi-channel network interface auditor designed to perform stealth port scanning against remote infrastructure endpoints. Leveraging low-level Python `socket` connections, the script executes TCP handshakes across key network ports, utilizes explicit connection timeout limits to handle packet drops gracefully, and maps exposed entry points based on structural return values.
* **Key Files:** `port_scanner.py` (Network socket scanner).

---

## 📂 Project 4: Cryptographic Password Strength & Policy Auditor
* **Directory Path:** [`/Password-Auditor-Lab`](./Password-Auditor-Lab)
* **Core Technical Domain:** Identity & Access Management (IAM) / Cryptographic Verification
* **Description:** Programmed an advanced local identity-vetting framework that conducts multidirectional validation on password inputs. The tool calculates absolute string entropy using character space permutations, checks lengths against strict corporate standards, and executes structural lookups against an integrated list of highly breached dictionary hashes to generate a complete defensive security risk score.
* **Key Files:** `password_auditor.py` (Policy script), `common_breaches.txt` (Breached signatures dictionary).

---

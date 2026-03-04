Hacmx 🔍

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue.svg">
  <img src="https://img.shields.io/badge/version-1.0.0-green.svg">
  <img src="https://img.shields.io/badge/license-MIT-blue.svg">
</p><p align="center">
  <b>OSINT & Security Recon Tool written in Python</b>
</p>---

📌 About

Hacmx is a modular OSINT and security reconnaissance toolkit designed for domain analysis and authorized security testing.

It provides DNS enumeration, SSL inspection, port scanning, GeoIP lookup, and a custom security scoring system.

---

⚡ Features

Feature| Description
🔎 DNS Enumeration| Resolve domain and gather DNS data
🌍 GeoIP Lookup| Detect hosting location and ISP
🔐 SSL Analysis| Inspect certificate validity & issuer
🚪 Port Scanner| Identify open ports
📡 Connectivity Monitor| Check domain/network availability
📊 Security Score| Risk-based scoring system
📄 Report Generator| Structured output report

---

🖥️ Dashboard Preview

«(You can add a screenshot here later)»

dashboard/
  ├── app.py
  ├── templates/
  └── static/

To add a screenshot later:

1. Take a screenshot
2. Upload to repo
3. Add:

![Dashboard](./dashboard_preview.png)

---

🚀 Installation

git clone https://github.com/Hacmx6/Hacmx.git
cd Hacmx
pip install -r requirements.txt

---

🧪 Usage

hacmx -d example.com --mode full

Example output includes:

- IP Address
- Reverse DNS
- Open Ports
- SSL Information
- GeoIP Data
- Security Score

---

📂 Project Structure

Hacmx/
│
├── dashboard/
├── modules/
├── main.py
├── setup.py
├── requirements.txt
└── README.md

---

🛣️ Roadmap

- [x] Core OSINT modules
- [x] Security scoring system
- [x] Dashboard interface
- [ ] Vulnerability pattern detection
- [ ] CVE lookup integration
- [ ] JSON export mode
- [ ] PyPI release

---

⚠️ Legal Notice

This tool is intended strictly for educational purposes and authorized security testing.

Unauthorized use against systems without permission may violate local laws.

---

👨‍💻 Author

Developed by Hacmx6

---

<p align="center">
  🚀 Built for learning • security • automation
</p>

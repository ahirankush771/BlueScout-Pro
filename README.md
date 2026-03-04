BlueScout Pro v3

Advanced Bluetooth Monitoring & Security Toolkit

Created by Ankush Kumar
Diploma CSE Student | Cybersecurity Learner

---

About This Project

BlueScout Pro v3 is an advanced Bluetooth monitoring toolkit designed for cybersecurity learners and developers.

The tool scans nearby Bluetooth devices, detects BLE devices, monitors them in real time, classifies device types, and exports scan reports for further analysis.

This project works on:

- Linux (Kali Linux / Ubuntu)
- Termux (Android)

The goal of this project is to help learners understand Bluetooth device discovery and wireless security monitoring.

---

Features

- Classic Bluetooth device scanning
- BLE (Bluetooth Low Energy) scanning
- Device type classification (mobile, computer, audio device etc.)
- RSSI signal strength detection
- Live monitoring mode
- Suspicious device detection alerts
- Device history logging
- JSON report export
- CSV report export
- Termux vibration and notification alerts
- Terminal UI dashboard using Rich library

---

Project Structure

BlueScout-Pro

BlueScout-Pro/
│
├── bluescout_pro.py
├── requirements.txt
└── README.md

---

Requirements

Python version:

Python 3.8 or higher

Required Python libraries:

pybluez
bleak
rich

---

Installation (Linux / Kali / Ubuntu)

Update system packages:

    sudo apt update

Install required system dependencies:

     sudo apt install python3 python3-pip bluetooth libbluetooth-dev

Clone the repository:

    git clone https://github.com/YOUR_USERNAME/BlueScout-Pro.git

Go to project folder:

    cd BlueScout-Pro

Install Python dependencies:

    pip3 install -r requirements.txt

Run the tool:

    sudo python3 bluescout_pro.py

---

Installation (Termux Android)

Update packages:

    pkg update
    pkg upgrade

Install required packages:

    pkg install python git termux-api

Clone the repository:

    git clone https://github.com/YOUR_USERNAME/BlueScout-Pro.git

Go to project directory:

    cd BlueScout-Pro

Install Python libraries:

    pip install -r requirements.txt

Run the tool:

    python bluescout_pro.py

---

Usage

Start the program:

    python bluescout_pro.py

Menu options:

1 Classic Bluetooth Scan
2 BLE Scan
3 Live Monitoring
4 Export JSON Report
5 Export CSV Report
6 Exit

---

Output Information

The tool displays:

Device MAC Address
Device Name
Device Type
RSSI Signal Strength
First Detection Time

Reports are saved as:

bluetooth_report.json
bluetooth_report.csv

These files contain full scan history for analysis.

---

Security Notice

This tool is created only for educational and defensive security research.

Do not use it for unauthorized monitoring, tracking, or illegal activities.

Always scan devices and networks that you own or have permission to test.

---

Developer Information

Name: Ankush Kumar

Course: Diploma in Computer Science & Engineering (CSE)

Field of Interest:

Cybersecurity
Ethical Hacking
Network Security
Linux System Security

This project is part of my cybersecurity learning journey where I build practical security tools and share them on GitHub.

---

Future Improvements

Planned upgrades for future versions:

Bluetooth device tracking system
Web dashboard interface
Real-time alert dashboard
Device analytics and statistics
Bluetooth signal distance estimation
Map visualization for device monitoring

---

License

This project is released under the MIT License.

---

Support

If you find this project useful:

Give it a star on GitHub
Share it with other cybersecurity learners
Contribute improvements to the project

---

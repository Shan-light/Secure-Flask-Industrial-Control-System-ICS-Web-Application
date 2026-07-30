# 🔐 Secure Flask Industrial Control System (ICS) Web Application

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Flask](https://img.shields.io/badge/Flask-Web%20Application-black)
![Security](https://img.shields.io/badge/Cybersecurity-Secure%20Coding-red)
![NIST](https://img.shields.io/badge/NIST-Compliant-green)
![OWASP](https://img.shields.io/badge/OWASP-Top%2010-orange)

---

## 📖 Table of Contents

- Project Overview
- Project Highlights
- Technologies Used
- Security Frameworks
- Application Features
- Security Controls
- System Architecture
- Threat Model
- Security Testing
- Application Walkthrough
- Key Takeaways
- Future Enhancements

---

# 📌 Project Overview

Designed and developed a secure **Industrial Control System (ICS)** web application using **Python** and **Flask** while integrating security throughout the **Secure Software Development Lifecycle (SSDLC)**.

The project demonstrates:

- Authentication
- Role-Based Access Control (RBAC)
- Audit Logging
- Secure Session Management
- Secure Coding Practices
- NIST Security Controls
- OWASP Top 10 Mitigations

---

# 🚀 Project Highlights

- ✔ Secure Flask Web Application
- ✔ Industrial Control System (ICS) Dashboard
- ✔ User Authentication
- ✔ Role-Based Access Control (RBAC)
- ✔ Microsoft SDL
- ✔ NIST SSDF
- ✔ OWASP Top 10
- ✔ Bandit Static Analysis
- ✔ Flawfinder Analysis
- ✔ OWASP ZAP Penetration Testing
- ✔ Security Logging
- ✔ Least Privilege

---

# 🛠 Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Backend Development |
| Flask | Web Framework |
| Bootstrap | Responsive User Interface |
| HTML/CSS | Front-End |
| CSV Files | Sensor Data Storage |
| Bandit | Static Code Analysis |
| Flawfinder | Source Code Analysis |
| OWASP ZAP | Penetration Testing |

---

# 🛡 Security Frameworks

- Microsoft Security Development Lifecycle (SDL)
- NIST Secure Software Development Framework (SSDF)
- FIPS 200
- OWASP Top 10
- NIST Security Controls

---

# ⚙️ Application Features

## 🔑 Authentication

- Secure Login
- Session Management
- Previous Login Notification
- Account Lockout

---

### ⚠ Security Warning Banner

Displays an authorized-use notice before authentication to inform users that:

- System activity is monitored
- Unauthorized access is prohibited
- User actions may be logged and audited
- Logging in constitutes consent to monitoring

This supports organizational security policies and user awareness by informing users that activity on the system is subject to monitoring.

---
## 👥 Role-Based Access Control

### User

- View ICS Data

### Administrator

- Manage Users
- Manage Sensor Data
- View Audit Logs

---

## 🌡 Industrial Control System Monitoring

Displays

- Temperature
- Humidity
- Timestamp

using environmental sensor data stored in a CSV file.

---

## 📝 Audit Logging

Administrator activity includes

- Timestamp
- IP Address
- HTTP Method
- Requested Page

---

## ⚙️ Administrative Functions

Administrators can

- Add Records
- Update Records
- Delete Records
- Unlock User Accounts

---

# 🔒 NIST Security Controls

| Control | Description |
|---------|-------------|
| AC-2 | Account Management |
| AC-6 | Least Privilege |
| AC-7 | Account Lockout |
| AC-9 | Previous Logon Notification |
| AU-2 | Event Logging |
| User Security Notice | Login banner informing users of monitoring and authorized use |
---

# 🏗 System Architecture

```text
                    +----------------------+
                    |      Web Browser     |
                    +----------+-----------+
                               |
                               |
                    HTTPS Requests
                               |
                               v
                  +-------------------------+
                  | Flask Web Application   |
                  +-----------+-------------+
                              |
          +-------------------+-------------------+
          |                   |                   |
          v                   v                   v
+----------------+   +----------------+   +----------------+
| Authentication |   | Session Mgmt   |   | Access Logging |
+----------------+   +----------------+   +----------------+
          |
          |
          v
+-----------------------------+
| Role-Based Access Control   |
+-------------+---------------+
              |
     +--------+---------+
     |                  |
     v                  v
+----------+     +----------------+
| ICS Data |     | Admin Functions|
+----------+     +----------------+
```

---

# ⚠ Threat Model

| Threat | Mitigation |
|---------|------------|
| Brute Force | Account Lockout |
| Unauthorized Access | RBAC |
| Session Hijacking | Secure Sessions |
| Privilege Escalation | Admin Authorization |
| Injection | Input Validation |
| Data Exposure | Authentication |
| Insider Threat | Audit Logging |

---

# 🔍 Security Testing

| Tool | Purpose |
|------|----------|
| Bandit | Python Static Security Analysis |
| Flawfinder | Source Code Vulnerability Analysis |
| OWASP ZAP | Dynamic Web Application Penetration Testing |

---

# 🖥 Application Walkthrough

## 🔐 Login Page

Users must authenticate before accessing protected resources. The login page displays a security warning informing users that the system is monitored and unauthorized access is prohibited.

**Key Security Features**
- Security warning banner
- Username and password authentication
- Role-based access control (RBAC)
- Secure session management
- Account lockout protection

> **Security Notice:** *This system is monitored. Unauthorized use is prohibited. By logging in, you consent to monitoring and auditing.*

![Login Page](https://github.com/Shan-light/Secure-Flask-Industrial-Control-System-ICS-Web-Application/blob/eb80a8fea9977c97cff32d2e5032dfc64fc666bf/Images/login%20page.jpg)

---

## 🏠 Home Dashboard

Displays the user's previous login, navigation menu, and quick-access cards.

![Home Dashboard](https://github.com/Shan-light/Secure-Flask-Industrial-Control-System-ICS-Web-Application/blob/93380833816a48630a920313c30f374d3129cb2c/Images/upper%20home%20page.jpg)

Lower home page

![lower home page](https://github.com/Shan-light/Secure-Flask-Industrial-Control-System-ICS-Web-Application/blob/0a6fa610f3c177cb503df81831fe1de8f8f51b7c/Images/lower%20home%20page.jpg )

---

## 🌡 ICS Monitoring

Displays environmental sensor readings while enforcing least privilege.

![ICS Monitoring](screenshots/ics-monitoring.png)

---

## 👥 User Management

Administrator page for managing users and unlocking accounts.

![Manage Users](screenshots/manage-users.png)

---

## ⚙️ Sensor Management

Administrators can create, update, and delete environmental sensor records.

![Manage Sensors](screenshots/manage-sensors.png)

---

## 📋 Audit Logs

Displays system activity including IP addresses, timestamps, and HTTP requests.

![Access Logs](screenshots/access-logs.png)

---

## ☁ Cloud Services

Overview of IaaS, SaaS, and Serverless Computing.

![Cloud Services](screenshots/cloud-services.png)

---

## ℹ About

Summarizes the application's purpose and implemented security controls.

![About Page](screenshots/about-page.png)

---

# 📚 Key Takeaways

- Integrated security throughout the Secure Software Development Lifecycle (SSDLC).
- Applied NIST security controls to a practical web application.
- Evaluated OWASP Top 10 security risks.
- Implemented authentication and role-based access control.
- Built comprehensive audit logging capabilities.
- Performed both static and dynamic security testing.
- Strengthened secure coding skills using Python and Flask.

---

# 🚀 Future Enhancements

- Multi-Factor Authentication (MFA)
- Password Hashing with bcrypt
- Database Integration (PostgreSQL)
- Docker Deployment
- HTTPS/TLS Configuration
- CI/CD Security Pipeline
- Automated Vulnerability Scanning
- Centralized Security Monitoring

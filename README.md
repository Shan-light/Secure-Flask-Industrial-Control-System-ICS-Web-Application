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

The application underwent both **Static Application Security Testing (SAST)** and **Dynamic Application Security Testing (DAST)** to identify security weaknesses before deployment.

| Tool | Type | Purpose | Key Findings |
|------|------|---------|--------------|
| Bandit | SAST | Python security analysis | Identified debug mode enabled and a hardcoded secret key. :contentReference[oaicite:0]{index=0} |
| Flawfinder | SAST | Source code analysis | Detected code quality and potential security issues requiring review. :contentReference[oaicite:1]{index=1} |
| OWASP ZAP | DAST | Web application penetration testing | Identified missing CSRF protection, CSP header, and anti-clickjacking headers. :contentReference[oaicite:2]{index=2} |

### Bandit Scan

![Bandit Scan](https://github.com/Shan-light/Secure-Flask-Industrial-Control-System-ICS-Web-Application/blob/70de07a3d46e4a14125b4de6c8f1dfffdc8ef71e/Images/bandit-result4pyFlask-app1.jpg)


### OWASP ZAP Scan

![OWASP ZAP Scan](https://github.com/Shan-light/Secure-Flask-Industrial-Control-System-ICS-Web-Application/blob/70de07a3d46e4a14125b4de6c8f1dfffdc8ef71e/Images/OWASP-ZAP-results.jpg)

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

![ICS Monitoring](https://github.com/Shan-light/Secure-Flask-Industrial-Control-System-ICS-Web-Application/blob/32bfc5840089df193df3703aea454f0707621952/Images/ICS%20page.jpg)

---

## 👥 User Management

Administrator page for managing users and unlocking accounts.

![Manage Users](https://github.com/Shan-light/Secure-Flask-Industrial-Control-System-ICS-Web-Application/blob/09f08d0d7242d8e7db53fce8858bf782adfeab5d/Images/manage%20user%20page.jpg)

---

## ⚙️ Sensor Management

Administrators can create, update, and delete environmental sensor records.

![Manage Sensors](https://github.com/Shan-light/Secure-Flask-Industrial-Control-System-ICS-Web-Application/blob/09f08d0d7242d8e7db53fce8858bf782adfeab5d/Images/sensor%20management%20page.jpg)

---

## 📋 Audit Logs

Displays system activity including IP addresses, timestamps, and HTTP requests.

![Access Logs](https://github.com/Shan-light/Secure-Flask-Industrial-Control-System-ICS-Web-Application/blob/09f08d0d7242d8e7db53fce8858bf782adfeab5d/Images/log%20info%20page.jpg)

---

## ☁ Cloud Services

Overview of IaaS, SaaS, and Serverless Computing.

![Cloud Services](https://github.com/Shan-light/Secure-Flask-Industrial-Control-System-ICS-Web-Application/blob/09f08d0d7242d8e7db53fce8858bf782adfeab5d/Images/cloud%20services%20page.jpg)

---

## ℹ About

Summarizes the application's purpose and implemented security controls.

![About Page](https://github.com/Shan-light/Secure-Flask-Industrial-Control-System-ICS-Web-Application/blob/09f08d0d7242d8e7db53fce8858bf782adfeab5d/Images/about%20webb-app%20page.jpg)

---

## 🚪 Logout

The Logout feature securely ends the user's session by clearing session data and redirecting the user to the login page. This helps prevent unauthorized access to protected resources after a session has ended.

**Key Security Features**

- Clears active session data
- Redirects users to the login page
- Prevents unauthorized access to protected pages after logout

![Logout Page](https://github.com/Shan-light/Secure-Flask-Industrial-Control-System-ICS-Web-Application/blob/09f08d0d7242d8e7db53fce8858bf782adfeab5d/Images/login%20page.jpg)

---

# 📚 Key Takeaways & Security Improvements

This project demonstrated the integration of security throughout the **Secure Software Development Lifecycle (SSDLC)** by applying **NIST security controls**, addressing **OWASP Top 10** risks, and implementing secure coding practices using **Python** and **Flask**.

Key accomplishments and improvements include:

- Integrated security throughout the Secure Software Development Lifecycle (SSDLC).
- Applied NIST security controls, including authentication, role-based access control (RBAC), least privilege, account lockout, and audit logging.
- Evaluated and mitigated common web application risks identified in the OWASP Top 10.
- Conducted both **Static Application Security Testing (SAST)** using Bandit and Flawfinder and **Dynamic Application Security Testing (DAST)** using OWASP ZAP.
- Identified and remediated security weaknesses, including disabling Flask debug mode for production, recommending secure storage of secret keys using environment variables, implementing CSRF protection, and strengthening HTTP security headers (Content Security Policy and X-Frame-Options).
- Strengthened practical skills in secure software development, security testing, vulnerability assessment, and secure web application design.

---

# 🚀 Future Enhancements

Future improvements to strengthen the application include:

- Replace CSV storage with a secure relational database (PostgreSQL or MySQL).
- Implement Multi-Factor Authentication (MFA) for enhanced user authentication.
- Enforce HTTPS/TLS for secure communication.
- Add CSRF protection to all forms using Flask-WTF.
- Configure security headers such as Content Security Policy (CSP) and X-Frame-Options.
- Integrate automated testing and CI/CD security scanning.
- Deploy the application using Docker and a production web server (Gunicorn with Nginx).

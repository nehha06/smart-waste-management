# Smart Waste Management System

## 1. Project Overview

The Smart Waste Management System is a web-based application designed to monitor municipal waste bins and support efficient waste collection.

The system stores waste-bin information, monitors fill levels and temperature, identifies abnormal conditions, assigns collection priority, and displays the information through a centralized dashboard.

## 2. Problem Statement

Traditional municipal waste collection often depends on manual monitoring and fixed collection schedules. This can result in overflowing bins, delayed collection, inefficient resource utilization, and reduced operational visibility.

This project provides a digital monitoring system that helps identify bins requiring attention and supports better collection decisions.

## 3. Objectives

- Monitor waste-bin fill levels.
- Store bin and alert information.
- Detect abnormal operating conditions.
- Assign collection priority.
- Provide a centralized dashboard.
- Provide REST API endpoints.
- Support containerized deployment.
- Maintain the project using Git and GitHub.

## 4. Key Features

- Waste-bin monitoring dashboard
- SQLite database
- Flask backend
- REST API
- Waste condition analysis
- Collection priority classification
- Alert monitoring
- Automated testing
- Docker containerization
- Git version control

## 5. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Application development |
| Flask | Backend web framework |
| SQLite | Database |
| HTML | Dashboard structure |
| CSS | Dashboard styling |
| pytest | Automated testing |
| Git | Version control |
| GitHub | Repository hosting |
| Docker | Application containerization |
| Docker Compose | Container management |

## 6. Repository Structure

```text
smart-waste-management/
│
├── app/
│   ├── app.py
│   ├── database.py
│   └── analysis.py
│
├── templates/
│   └── dashboard.html
│
├── static/
│   └── style.css
│
├── tests/
│   └── test_app.py
│
├── database/
│   └── waste.db
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── README.md
└── .gitignore
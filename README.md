# Smart Waste Management System

A full-stack Smart Waste Management System developed using Flask, SQLite, HTML, CSS, REST APIs, automated testing, and Docker.

The system helps monitor waste-bin conditions, identify high-priority bins, generate alerts, and analyze waste levels based on fill level and temperature.

## 1. Problem Overview

Traditional waste collection systems often depend on fixed collection schedules. This can result in:

- Overflowing waste bins
- Unnecessary collection trips
- Delayed response to abnormal bin conditions
- Poor monitoring of waste levels
- Increased operational cost

The Smart Waste Management System provides a centralized dashboard for monitoring waste bins and identifying bins that require attention.

## 2. Project Objectives

The main objectives are:

- Monitor waste-bin fill levels.
- Store bin information in a database.
- Identify high-priority waste bins.
- Detect abnormal bin conditions.
- Generate alerts for waste-management staff.
- Provide REST APIs for accessing bin data.
- Perform waste-condition analysis.
- Provide a web-based monitoring dashboard.
- Validate application functionality through automated tests.
- Containerize the application using Docker.

## 3. Key Features

### Dashboard

The dashboard displays:

- Total number of bins
- High-priority bins
- Normal bins
- Total alerts
- Bin ID
- Location
- Fill level
- Temperature
- Condition
- Priority
- System status

### Database Management

The system uses SQLite to store waste-bin information.

Each bin contains:

- Bin ID
- Location
- Fill level
- Temperature
- Condition
- Priority

### Waste Analysis

The analysis module evaluates:

- Fill level
- Temperature
- Bin condition
- Priority level

The system identifies abnormal and high-priority bins.

### REST APIs

The backend provides APIs for:

- Bin information
- Alert information
- Waste analysis results

### Automated Testing

Pytest validates:

- Dashboard availability
- Bin API
- Alerts API
- Waste analysis API

### Docker Containerization

The application uses:

- Dockerfile
- Docker Compose

## 4. System Architecture

```text
                 USER
                  |
                  v
        +--------------------+
        | Web Dashboard      |
        | HTML + CSS         |
        +--------------------+
                  |
                  v
        +--------------------+
        | Flask Backend      |
        | app.py             |
        +--------------------+
             |          |
             v          v
     +-----------+   +-------------+
     | Analysis  |   | REST APIs   |
     | Module    |   | /api/bins   |
     +-----------+   | /api/alerts |
             |       | /api/analyze|
             |       +-------------+
             |
             v
       +-------------+
       | SQLite      |
       | Database    |
       +-------------+
```

## 5. Technology Stack

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Flask | Web framework and REST API |
| SQLite | Database |
| HTML | Frontend structure |
| CSS | Frontend styling |
| Jinja2 | Dynamic HTML rendering |
| Pytest | Automated testing |
| Docker | Application containerization |
| Docker Compose | Container management |
| Git | Version control |
| GitHub | Repository hosting |

## 6. Repository Structure

```text
smart-waste-management/
|
|-- app/
|   |-- app.py
|   |-- analysis.py
|   `-- database.py
|
|-- static/
|   `-- style.css
|
|-- templates/
|   `-- dashboard.html
|
|-- tests/
|   `-- test_app.py
|
|-- .gitignore
|-- Dockerfile
|-- docker-compose.yml
|-- README.md
`-- requirements.txt
```

The SQLite database file is generated locally when the application runs and is excluded from Git tracking using `.gitignore`.

## 7. Module Description

### app.py

The main Flask application.

Responsibilities:

- Initialize Flask.
- Connect frontend and backend.
- Retrieve data from the database.
- Render the dashboard.
- Provide REST API endpoints.
- Process waste-analysis requests.

### database.py

Responsible for database operations.

Responsibilities:

- Create the SQLite database.
- Create required tables.
- Insert initial waste-bin data.
- Establish database connections.
- Retrieve database records.

### analysis.py

Responsible for waste-condition analysis.

Responsibilities:

- Analyze fill levels.
- Analyze temperature.
- Determine bin condition.
- Determine priority.
- Generate analysis results.

### dashboard.html

The main frontend dashboard.

### style.css

Provides the visual design of the dashboard.

### test_app.py

Contains automated test cases for validating backend functionality.

## 8. Database Design

The system uses SQLite as its database.

### Bin Data

| Field | Description |
|---|---|
| id | Unique database ID |
| bin_id | Unique bin identifier |
| location | Location of the bin |
| fill_level | Percentage of bin filled |
| temperature | Temperature recorded |
| condition | Current bin condition |
| priority | Priority for collection |

Example:

```text
B101 | Zone 1 | 92% | 35 C | NORMAL   | HIGH
B102 | Zone 2 | 68% | 32 C | NORMAL   | LOW
B103 | Zone 3 | 81% | 37 C | NORMAL   | MEDIUM
B104 | Zone 4 | 95% | 70 C | ABNORMAL | HIGH
```

## 9. REST API Endpoints

### Get All Bins

```text
GET /api/bins
```

Returns waste-bin information in JSON format.

### Get Alerts

```text
GET /api/alerts
```

Returns bins requiring attention based on their condition or priority.

### Waste Analysis

```text
GET /api/analyze/<fill_level>/<temperature>
```

Example:

```text
GET /api/analyze/95/70
```

Example response:

```json
{
    "condition": "ABNORMAL",
    "priority": "HIGH"
}
```

## 10. How the System Works

```text
1. User opens the dashboard
          |
          v
2. Flask receives the request
          |
          v
3. Backend connects to SQLite
          |
          v
4. Waste-bin data is retrieved
          |
          v
5. Analysis module evaluates conditions
          |
          v
6. Backend calculates priority and alerts
          |
          v
7. Results are sent to the dashboard
          |
          v
8. User views waste-management status
```

## 11. Installation

### Prerequisites

Install:

- Python 3.x
- Git
- Docker Desktop

## 12. Run the Project Locally

Clone the repository:

```bash
git clone https://github.com/nehha06/smart-waste-management.git
```

Move into the project directory:

```bash
cd smart-waste-management
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the Flask application:

```bash
python app/app.py
```

Open:

```text
http://localhost:5000
```

## 13. Run Using Docker

Make sure Docker Desktop is running.

Build and start:

```bash
docker compose up --build
```

Open:

```text
http://localhost:5000
```

Check the container:

```bash
docker compose ps
```

Stop the application:

```bash
docker compose down
```

## 14. Testing

The project uses Pytest for automated testing.

Install Pytest:

```bash
python -m pip install pytest
```

Run all tests:

```bash
python -m pytest -v
```

Expected result:

```text
tests/test_app.py::test_home_page PASSED
tests/test_app.py::test_bins_api PASSED
tests/test_app.py::test_alerts_api PASSED
tests/test_app.py::test_waste_analysis PASSED

4 passed
```

### Test Cases

| Test Case | Purpose | Expected Result |
|---|---|---|
| test_home_page | Checks dashboard | PASS |
| test_bins_api | Checks bin API | PASS |
| test_alerts_api | Checks alerts API | PASS |
| test_waste_analysis | Checks analysis API | PASS |

## 15. Code Quality

The project follows basic software-engineering practices:

- Modular Python files
- Meaningful file names
- Separation of frontend and backend
- Database operations separated from application logic
- Analysis logic separated into its own module
- Automated tests
- Dependency management
- Version control using Git
- Containerization using Docker

## 16. Version Control

Git is used for source-code management and GitHub is used as the remote repository.

The repository contains multiple commits representing different development stages.

Example development history:

```text
Initial Flask application setup
        |
        v
Add waste analysis and Docker configuration
        |
        v
Add waste management dashboard
        |
        v
Add backend testing and project documentation
        |
        v
Exclude generated database from repository
        |
        v
Update gitignore for database and test files
```

Version control helps with:

- Tracking changes
- Maintaining project history
- Recovering previous versions
- Supporting collaboration
- Managing project development

## 17. Docker Architecture

```text
          Docker Compose
                |
                v
      +-------------------+
      | Smart Waste App   |
      | Flask Container   |
      +-------------------+
          |           |
          v           v
     Flask App     SQLite
          |
          v
      Port 5000
          |
          v
       Browser
```

## 18. Validation

The application was validated using:

- Browser-based dashboard testing
- REST API testing
- Database verification
- Automated Pytest testing
- Docker container execution

The automated test suite verifies the major application routes and confirms that the backend responds correctly.

## 19. Future Enhancements

Possible future improvements:

- Real-time IoT sensor integration
- GPS-based bin tracking
- Live fill-level monitoring
- User authentication
- Admin dashboard
- Waste collection route optimization
- Email/SMS alerts
- Data visualization and charts
- PostgreSQL or MySQL support
- Cloud deployment
- Machine-learning based waste prediction

## 20. Conclusion

The Smart Waste Management System demonstrates a full-stack software application combining a web frontend, Flask backend, SQLite database, REST APIs, analysis logic, automated testing, Git version control, and Docker containerization.

The project provides a structured foundation for monitoring waste bins and supporting efficient waste-collection decisions.

## 21. Project Repository

GitHub:

https://github.com/nehha06/smart-waste-management

## 22. Author

**Neha**

B.Tech - Artificial Intelligence and Machine Learning

Saveetha School of Engineering

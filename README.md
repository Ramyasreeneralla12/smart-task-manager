# Smart Task Management System

## Live Demo
https://smart-task-manager-4dv4.onrender.com

---

# Project Overview
Smart Task Management System is a full-stack Flask web application developed to manage daily tasks efficiently with real-time notifications, analytics, and responsive UI support.

The project demonstrates practical implementation of:
- Python
- Flask
- REST APIs
- PostgreSQL
- Pandas & NumPy
- WebSockets
- HTML/CSS

---

# Features

## Authentication
- User Registration
- User Login
- Logout Functionality
- Secure Password Hashing

## Task Management
- Add Task
- Update Task
- Delete Task
- Mark Task as Completed
- Deadline Management
- Task History

## Analytics Dashboard
- Total Tasks
- Completed Tasks
- Pending Tasks
- Completion Percentage

## Real-Time Notifications
- Live Task Updates
- Completion Alerts
- Real-Time Dashboard Notifications

## Responsive UI
- Mobile Friendly
- Tablet Responsive
- Desktop Support
- Modern Dashboard Design

---

# Technologies Used

## Backend
- Python
- Flask
- Flask-SQLAlchemy
- Flask-Login
- Flask-Bcrypt
- Flask-SocketIO

## Frontend
- HTML
- CSS
- JavaScript

## Database
- PostgreSQL

## Analytics
- Pandas
- NumPy

## Deployment
- Render

---

# REST APIs

| API Endpoint | Method | Description |
|---|---|---|
| /add-task | POST | Add New Task |
| /update-task/<id> | POST | Update Task |
| /delete-task/<id> | GET | Delete Task |
| /api/tasks | GET | Get All Tasks |

---

# Installation

```bash
git clone https://github.com/Ramyasreeneralla12/smart-task-manager.git

cd smart-task-manager

python -m venv .venv

.venv\Scripts\activate

pip install -r requirements.txt

python app.py
```

---

# Project Structure

```text
smart-task-manager/

├── app.py
├── config.py
├── models/
├── routes/
├── templates/
├── static/
├── analytics/
├── websocket/
└── database/
```

---
# Future Improvements

- Email Notifications
- AI-Based Task Suggestions
- Calendar Integration
- Dark Mode
- Multi-User Collaboration

---
# Conclusion

This project demonstrates full-stack web development using Flask, PostgreSQL, REST APIs, WebSockets, and responsive frontend technologies with real-time functionality and analytics support.

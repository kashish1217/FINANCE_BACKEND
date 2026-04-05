# 💰 Finance Dashboard Backend

## 📌 Overview

This project is a backend system for managing financial records with role-based access control and analytics.

It provides secure APIs for handling transactions (income/expense), along with a dashboard summary including totals, category breakdown, and monthly trends.

---

## 🚀 Features

### 👤 User & Role Management

* Custom user model
* Roles:

  * **Admin** → Full access (CRUD)
  * **Analyst** → Read + analytics
  * **Viewer** → Restricted access
* Role-based permissions implemented

---

### 💰 Financial Records API

* Create, update, delete records (Admin only)
* View records (Analyst/Admin)
* Fields:

  * amount
  * type (income / expense)
  * category
  * date
  * notes
* Each record linked to a user

---

### 📊 Dashboard Summary API

Endpoint: `/api/summary/`

Provides:

* Total Income
* Total Expense
* Net Balance
* Category-wise breakdown
* Recent transactions
* Monthly trends

---

### 🔐 Authentication

This project uses **JWT (JSON Web Token)** authentication.

#### Get Token:

POST /api/token/

#### Use Token:

Authorization: Bearer <your_access_token>

---

## 🛠️ Tech Stack

* Python
* Django
* Django REST Framework
* SimpleJWT (Authentication)
* SQLite (can be replaced with PostgreSQL)

---

## ⚙️ Setup Instructions

# Clone repository
git clone https://github.com/<your-username>/finance-dashboard-backend.git
cd finance-dashboard-backend

# Create virtual environment
python -m venv venv
venv\Scripts\activate   # Windows

# Install dependencies
python -m pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Create admin user
python manage.py createsuperuser

# Run server
python manage.py runserver

---

## 🔗 API Endpoints

| Endpoint      | Method | Description           |
| ------------- | ------ | --------------------- |
| /api/token/   | POST   | Get JWT token         |
| /api/records/ | GET    | List records          |
| /api/records/ | POST   | Create record (Admin) |
| /api/summary/ | GET    | Dashboard summary     |

---

## 📊 Sample Response

json
{
  "status": "success",
  "data": {
    "total_income": 5000,
    "total_expense": 2000,
    "net_balance": 3000,
    "category_breakdown": {
      "salary": 5000,
      "food": 2000
    },
    "recent_transactions": [],
    "monthly_trends": []
  }
}


---

## 🌐 Live API

(Add your deployment link here after deploying)

https://your-app.onrender.com

---

## 🧠 Assumptions

* Roles are assigned via admin panel
* Authentication handled via JWT
* SQLite used for simplicity (can scale to PostgreSQL)

---

## 📌 Future Improvements

* Pagination
* Advanced filtering
* Search functionality
* PostgreSQL integration
* Docker deployment

---

## 👨‍💻 Author

Abhay Sinha

---

## 📌 Note

This project focuses on clean backend architecture, secure authentication, and scalable API design rather than unnecessary complexity.

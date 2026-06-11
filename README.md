# Django Assignment — Users & Products Web Application

A Django web application built as part of a backend development assignment.
The project contains **two apps** (Users and Products) inside a single Django project,
each connected to their own **separate database**.

---

## 📁 Project Structure

```
django_assignment/
├── core/                  → Project settings, URLs, database router
├── users/                 → App 1: User & Post models, authentication
├── products/              → App 2: Product model
├── templates/             → HTML templates
├── manage.py
├── requirements.txt
└── README.md
```

---

## ✅ Features

- **Users App**
  - Register a new account
  - Login / Logout
  - Create posts (authenticated users only)
  - User and Post models with model-level relationship (no DB-level foreign key)

- **Products App**
  - Product model with name, weight, and price
  - Runs on a completely separate database

- **Admin Dashboard**
  - User, Post, and Product all registered and manageable from `/admin/`

- **Two Separate Databases**
  - `db_users.sqlite3` → for Users app
  - `db_products.sqlite3` → for Products app

---

## 🛠️ Tech Stack

- Python 3.x
- Django 4.2
- SQLite (two separate databases)
- HTML / CSS (custom templates)

---

## ⚙️ Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/Divyanshi8081/django_assignment.git
cd django_assignment
```

### 2. Create and activate virtual environment
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run migrations
```bash
python manage.py migrate
python manage.py migrate --database=products_db
```

### 5. Create superuser (for admin access)
```bash
python manage.py createsuperuser
```

### 6. Start the server
```bash
python manage.py runserver
```

---

## 🌐 URLs

| URL | Description |
|-----|-------------|
| `http://127.0.0.1:8000/` | Redirects to Login |
| `http://127.0.0.1:8000/users/register/` | Register a new account |
| `http://127.0.0.1:8000/users/login/` | Login |
| `http://127.0.0.1:8000/users/create-post/` | Create a post (login required) |
| `http://127.0.0.1:8000/admin/` | Admin dashboard |

---

## 🗄️ Models

### Users App

**User**
| Field | Type |
|-------|------|
| first_name | CharField |
| last_name | CharField |
| email | EmailField |
| password | CharField |
| username | CharField |

**Post**
| Field | Type |
|-------|------|
| user | IntegerField (model-level FK only) |
| text | TextField |
| created_at | DateTimeField |
| updated_at | DateTimeField |

### Products App

**Product**
| Field | Type |
|-------|------|
| name | CharField |
| weight | DecimalField |
| price | DecimalField |
| created_at | DateTimeField |
| updated_at | DateTimeField |

---

## 👩‍💻 Author

**Divyanshi**
GitHub: [@Divyanshi8081](https://github.com/Divyanshi8081)

# 🚀 Content API CMS

A premium, headless-ready Content Management System built with Django, Django Rest Framework (DRF), and Wagtail. This project combines a modern, high-performance UI with a robust API, making it suitable for both traditional web serving and headless content delivery.

![Dashboard Preview](https://via.placeholder.com/800x400?text=Premium+CMS+Dashboard)

## ✨ Key Features

- **🎨 Premium UI Design**: A completely custom, responsive design system using modern CSS variables, glassmorphism, and smooth animations. No generic Bootstrap/Tailwind look.
- **🔌 Hybrid Architecture**: Functions as both a traditional Django web app and a headless API. The frontend dynamically communicates with the backend API.
- **🔐 Secure Authentication**: 
    - Full user registration and login flow with secure password hashing.
    - Dual authentication support: **Session** (for browser) and **Token** (for API clients).
    - Role-based access control.
- **🦅 Wagtail CMS Integration**: Enterprise-grade page management capabilities built-in.
- **⚡ High Performance**: Optimized database queries and efficient static file serving.
- **🛠️ Developer Tools**: Includes automated performance benchmarking scripts and a ready-to-use Postman collection.

## 🛠️ Tech Stack

- **Backend**: Python 3.x, Django 5.x
- **API**: Django Rest Framework (DRF)
- **CMS**: Wagtail
- **Frontend**: HTML5, Vanilla CSS3 (Custom Design System), Vanilla JavaScript (ES6+)
- **Database**: SQLite (Default) / PostgreSQL (Production ready)

## 🚀 Getting Started

Follow these steps to set up the project locally.

### Prerequisites
- Python 3.8 or higher
- Git

### Installation

1. **Clone the Repository**
   ```bash
   git clone <your-repo-url>
   cd content_api
   ```

2. **Create a Virtual Environment**
   ```bash
   python -m venv django_venv
   # Windows
   django_venv\Scripts\activate
   # Mac/Linux
   source django_venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create Superuser**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the Server**
   ```bash
   python manage.py runserver
   ```
   Visit `http://127.0.0.1:8000/` to see the application.

## 📖 API Documentation

The API is accessible at `/content/api/`. It supports both Session and Token authentication.

### Authentication Endpoints
- **Register**: `POST /content/register/`
- **Login**: `POST /content/api/login/` (Returns Auth Token)

### Content Endpoints
- **List Items**: `GET /content/api/items/`
- **Create Item**: `POST /content/api/items/`
- **Retrieve Item**: `GET /content/api/items/{id}/`
- **Update Item**: `PUT /content/api/items/{id}/`
- **Delete Item**: `DELETE /content/api/items/{id}/`

### 🧪 Testing & Tools

#### Postman Collection
A `postman_collection.json` file is included in the root directory. Import it into Postman to instantly test all API endpoints.

#### Performance Benchmark
Run the included performance test script to benchmark the API's response times:
```bash
python test_performance.py
```
*Sample Output:*
```
Register: 0.4260s - Status: 200
Login:    0.3903s - Status: 200
Create:   0.0225s - Status: 201
...
```

## 📂 Project Structure

```
content_api/
├── CONTENT_APP/            # Main application app
│   ├── templates/          # HTML Templates (Premium UI)
│   ├── static/             # CSS & Assets
│   ├── models.py           # Database Models
│   ├── views.py            # UI Views & API ViewSets
│   ├── serializers.py      # DRF Serializers
│   └── urls.py             # App Routing
├── content_api/            # Project configuration
│   ├── settings.py         # Global Settings
│   └── urls.py             # Main URL configuration
├── manage.py               # Django CLI utility
├── postman_collection.json # API Test Collection
└── test_performance.py     # Performance Script
```

## 🤝 Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

---
*Built with ❤️ by [Your Name]*
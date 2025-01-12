# Recipe Management API

## Overview
The Recipe Management API is a Django-based backend system that allows users to manage recipes by creating, updating, deleting, and viewing them by categories or ingredients. The API is built using Django and Django REST Framework (DRF) and includes features like authentication, permission management, and filtering.

## Features
- Full CRUD operations for recipes
- User authentication and permissions
- Filtering recipes by category or ingredient
- Token-based authentication using JWT
- Pagination and sorting for large datasets

## API Routes
### Recipe Endpoints
| Endpoint                              | HTTP Method | Description                         |
|---------------------------------------|-------------|-------------------------------------|
| `/api/recipes/`                       | GET         | List all recipes                   |
| `/api/recipes/`                       | POST        | Create a new recipe                |
| `/api/recipes/<id>/`                  | GET         | Retrieve a recipe by ID            |
| `/api/recipes/<id>/`                  | PUT         | Update a recipe                    |
| `/api/recipes/<id>/`                  | DELETE      | Delete a recipe                    |
| `/api/recipes/category/<category>/`   | GET         | Filter recipes by category         |
| `/api/recipes/ingredient/<ingredient>/`| GET         | Filter recipes by ingredient        |

### Authentication Endpoints
| Endpoint          | HTTP Method | Description                         |
|-------------------|-------------|-------------------------------------|
| `/api/token/`     | POST        | Obtain JWT access and refresh tokens |
| `/api/token/refresh/` | POST   | Refresh the access token            |

## Steps to Run the Project

### Prerequisites
- Python 3.8+
- pip
- Git
- PostgreSQL or SQLite (default database)

### Local Setup
1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd recipe_management_api
   ```

2. **Set Up a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**
   Create a `.env` file in the project root and define the following:
   ```env
   SECRET_KEY=your_django_secret_key
   DEBUG=True
   DATABASE_URL=sqlite:///db.sqlite3
   ```

5. **Apply Migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Run the Development Server**
   ```bash
   python manage.py runserver
   ```
   The server will be available at `http://127.0.0.1:8000/`.

### Testing the API
1. **Create a Superuser**
   ```bash
   python manage.py createsuperuser
   ```
   Follow the prompts to set up an admin account.

2. **Access the Django Admin Panel**
   Navigate to `http://127.0.0.1:8000/admin` and log in with the superuser credentials.

3. **Test Endpoints**
   Use tools like [Postman](https://www.postman.com/) or `curl` to interact with the API.



## Reflection
This project was selected because it provides practical experience in backend development with Django and Django REST Framework. The focus on authentication, filtering, and efficient data management simulates real-world development challenges and solutions.

---




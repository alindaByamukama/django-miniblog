### Project Description: MiniBlog

**Django Miniblog is a simple blogging api** built using the Django web framework and Django REST framework. It allows users to create, read, update, and delete blog posts, providing a basic platform for content management and publication. The application is designed with RESTful API endpoints to facilitate seamless integration with various front-end frameworks or client applications.

**Demo**: [django-miniblog live link](https://django-miniblog.onrender.com)

#### Features

1. **User Authentication**:
   - Secure user registration and login functionality.
   - Token-based authentication for secure API access.

2. **Blog Post Management**:
   - Create, read, update, and delete (CRUD) operations for blog posts.
   - Each blog post includes a title, content, publication date, and author information.
   - Authors can only edit or delete their own posts, ensuring content integrity.

3. **API Endpoints**:
   - RESTful API endpoints for managing users and blog posts.
   - Hyperlinked relationships between users and their respective blog posts.
   - Search functionality to find blog posts by author or title.

4. **Security Features**:
   - HTTPS enforcement and secure cookies to protect data in transit.
   - CSRF protection to prevent cross-site request forgery attacks.
   - Configurable login attempt limits to mitigate brute force attacks.

5. **Testing**:
   - Comprehensive unit tests for models, serializers, and views.
   - Utilizes `pytest` and `pytest-django` for efficient test execution and coverage.

#### Technical Stack

- **Backend**: Django, Django REST framework
- **Database**: SQLite (default, easily switchable to other databases like PostgreSQL)
- **Authentication**: Django Token Authentication
- **Testing**: pytest, pytest-django
- **Documentation**: Swagger (drf-yasg)

## Getting Started

### Clone the repository:

```bash
git clone https://github.com/yourusername/miniblog.git
cd miniblog
```

### Create and activate a virtual environment:

```bash
python3 -m venv env
source env/bin/activate
```

### Install the dependencies:

```bash
pip install -r requirements.txt
```

### Apply migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

### Run the development server:

```bash
python manage.py runserver
```

### Run the tests:

```bash
pytest
```

## Usage

### Access the API:

The API endpoints can be accessed at `http://127.0.0.1:8000/`.

Example endpoints:
- `http://127.0.0.1:8000/blogposts/` - List and create blog posts.
- `http://127.0.0.1:8000/users/` - List and create users.

### Authentication:

- Obtain a token by providing valid credentials to the login endpoint.
- Use the token to access protected endpoints.

### Documentation:

- Swagger UI: `http://127.0.0.1:8000/swagger/`
- ReDoc: `http://127.0.0.1:8000/redoc/`

## Contributing

Contributions are welcome! Please fork the repository and submit pull requests with improvements or bug fixes. Ensure all tests pass and code is well-documented.

---

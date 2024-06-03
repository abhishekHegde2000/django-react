# FILE: requirements.md

Here's a breakdown of each package in your `requirements.txt` file:

1. `asgiref`: This is the ASGI (Asynchronous Server Gateway Interface) reference server. It's used by Django to handle asynchronous requests.
2. `Django`: This is the main Django package. Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design.
3. `django-cors-headers`: This is a Django App that adds Cross-Origin Resource Sharing (CORS) headers to your project. CORS headers allow your Django backend to accept requests from a different origin (domain, scheme, or port) than its own.
4. `djangorestframework`: This is a powerful and flexible toolkit for building Web APIs in Django. It's used to create APIs that can be consumed by frontend applications or other services.
5. `djangorestframework-simplejwt`: This is a JSON Web Token authentication plugin for the Django REST Framework. It provides views for obtaining, refreshing, and verifying JWT tokens.
6. `PyJWT`: This is a Python library which allows you to encode, decode, verify signatures and claims of JWT tokens.
7. `pytz`: This is a Python library that allows accurate and cross-platform timezone calculations.
8. `sqlparse`: This is a non-validating SQL parser module for Python. It provides support for parsing, splitting and formatting SQL statements.
9. `psycopg2-binary`: This is a PostgreSQL adapter for Python. It's used by Django to connect to your PostgreSQL database.
10. `python-dotenv`: This library allows you to specify environment variables in a .env file. This can be useful for managing secrets or configuration settings that shouldn't be checked into source control.

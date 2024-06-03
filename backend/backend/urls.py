from django.contrib import admin
from django.urls import path, include
from api.views import CreateUserView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/user/register/", CreateUserView.as_view(), name="register"),
    path("api/token/", TokenObtainPairView.as_view(), name="get_token"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="refresh"),
    path("api-auth/", include("rest_framework.urls")),
    path("api/", include("api.urls")),
]


'''

1. `from django.contrib import admin`: This import is for Django's built-in admin interface. It's a powerful feature that allows you to create, read, update, and delete records. In the `urlpatterns`, you can see `path("admin/", admin.site.urls)`, which means if you go to `<your-domain>/admin/`, you'll see the admin interface.

2. `from django.urls import path, include`: These are functions to define the routes for your application. `path` is used to map a URL pattern to a view, while `include` is used to include other URL configurations. In your `urlpatterns`, you're using `path` to define routes like `admin/`, `api/user/register/`, etc., and `include` to include additional routes defined in `rest_framework.urls` and `api.urls`.

3. `from api.views import CreateUserView`: This is importing a view you've defined in your `api` app. A view is a Python function that takes a web request and returns a web response. `CreateUserView` is likely a view that handles user registration. It's used in the route `api/user/register/`.

4. `from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView`: These are views provided by the `rest_framework_simplejwt` package, a JSON Web Token authentication plugin for the Django REST Framework. `TokenObtainPairView` is used to obtain a pair of JWT tokens (access and refresh) using your login credentials. `TokenRefreshView` is used to obtain a new access token using a refresh token. These are used in the routes `api/token/` and `api/token/refresh/`.

In a real-world case, you'd use these imports to set up your web application's routes. For example, you might have a blog application, and you'd use `path` to define routes for viewing the blog list, creating a new blog, editing a blog, etc. You'd use `include` to separate the blog-related routes into their own URL configuration for better organization. You'd use views to define what happens when a user visits those routes - maybe they see a list of blogs, or a form to create a new blog. If your application has user registration, you'd create a view for that and map it to a URL with `path`, just like `CreateUserView` is mapped here. If your application has an API that uses JWT for authentication, you'd use `TokenObtainPairView` and `TokenRefreshView` to handle token generation and refreshing.
'''


'''
```python
from django.contrib import admin
```
This import brings in Django's built-in admin module. It's used to create an administration interface for managing your site's data. For example, if you have models (database tables) defined in your Django application, you can register them with the admin site to easily create, read, update, and delete (CRUD) records.

```python
from django.urls import path, include
```
This import brings in utilities for URL routing in Django. `path` is used to define URL patterns, and `include` is used to include other URL configurations from other apps. In simpler terms, `path` helps map URLs to views in your application, while `include` helps include URLs from other parts of your project.

```python
from api.views import CreateUserView
```
This import is bringing in a specific view called `CreateUserView` from the `api` app. In Django, views are Python functions or classes that handle web requests and return web responses. `CreateUserView` is likely a custom view defined in your project that handles user registration.

```python
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
```
These imports are for JWT (JSON Web Token) authentication views provided by the `rest_framework_simplejwt` package. JWT is a popular way to handle authentication in web applications. `TokenObtainPairView` is used to obtain a new access and refresh token pair by exchanging a username and password for a valid user, and `TokenRefreshView` is used to refresh an access token.

```python
path("admin/", admin.site.urls),
```
This line defines a URL pattern that routes requests with the URL path `admin/` to the Django admin site. `admin.site.urls` is where Django's admin site is mounted.

```python
path("api/user/register/", CreateUserView.as_view(), name="register"),
```
This line defines a URL pattern that routes requests with the URL path `api/user/register/` to the `CreateUserView` view. When a request matches this pattern, Django will call the `as_view()` method on `CreateUserView` to convert it into a view function.

```python
path("api/token/", TokenObtainPairView.as_view(), name="get_token"),
```
This line defines a URL pattern that routes requests with the URL path `api/token/` to the `TokenObtainPairView` view, which is responsible for generating JWT tokens for authentication.

```python
path("api/token/refresh/", TokenRefreshView.as_view(), name="refresh"),
```
This line defines a URL pattern similar to the previous one but routes requests to the `TokenRefreshView` view. This view is used to refresh an existing JWT access token.

```python
path("api-auth/", include("rest_framework.urls")),
```
This line includes URLs for built-in authentication views provided by Django REST Framework. These views are useful for handling authentication-related endpoints like login, logout, and password reset.

```python
path("api/", include("api.urls")),
```
This line includes URLs from another URL configuration file (`api.urls`). This allows you to organize your URL patterns into separate files for better maintainability.

In real-world scenarios, these imports and URL patterns are used to create a web application with user registration, authentication using JWT tokens, and an admin interface for managing site data. For instance, you might use the `CreateUserView` to allow users to register on your site, JWT tokens for user authentication, and Django's admin site to manage user data and other site resources.
'''

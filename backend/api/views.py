'''

The imports in this Python file are used for various purposes in a Django and Django REST framework application. Here's a breakdown:

1. `from django.shortcuts import render`: This is a shortcut function to render templates. It takes a request and a template name, then returns an HttpResponse object with that rendered text. In real-world cases, it's used to display HTML pages.

2. `from django.contrib.auth.models import User`: This is Django's built-in User model. It's used for user authentication and management. In real-world cases, it's used to handle user data like usernames, passwords, emails, etc.

3. `from rest_framework import generics`: This is a part of Django REST framework that provides generic class-based views. It's used to quickly build API views around standard create/retrieve/update/delete operations. In real-world cases, it's used to create API endpoints.

4. `from .serializers import UserSerializer, NoteSerializer`: Serializers in Django REST framework allow complex data types, like querysets and model instances, to be converted to Python native datatypes that can then be easily rendered into JSON, XML, or other content types. In real-world cases, `UserSerializer` and `NoteSerializer` are used to serialize User and Note model instances respectively.

5. `from rest_framework.permissions import IsAuthenticated, AllowAny`: These are permission classes in Django REST framework. `IsAuthenticated` ensures that the user is authenticated before they can access the view, while `AllowAny` allows unrestricted access, regardless of authentication. In real-world cases, they're used to control access to API views.

6. `from .models import Note`: This is importing the Note model from the models.py file in the same directory. In real-world cases, the Note model might be used to store and manage notes or similar data for users.


'''


from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, NoteSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Note


class CreateUserView(generics.CreateAPIView):
    """
    API endpoint to create a new user.

    This view class inherits from the CreateAPIView class provided by the
    Django REST framework. It allows users to create a new user by sending
    a POST request with the required user data.

    Attributes:
        queryset (QuerySet): The queryset of User objects.
        serializer_class (class): The serializer class for User objects.

    """

    # list of all different objects we will look while creating a new user
    queryset = User.objects.all()
    # connecting our auth routes , its a serialiser class that will tell us what kind of data we are expecting to create a new user
    serializer_class = UserSerializer
    permission_classes = [AllowAny]  # Allow any user to create a new user

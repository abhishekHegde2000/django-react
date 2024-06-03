from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Note


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer class for the User model.

    This serializer is used to convert User model instances to JSON
    representation and vice versa. It specifies the fields to be included
    in the serialized output and provides validation for the input data.

    Attributes:
        model (class): The User model class.
        fields (list): The fields to be included in the serialized output.
        extra_kwargs (dict): Additional keyword arguments for field options.

    Methods:
        create(validated_data): Create a new User instance based on the
            validated data.

    """

    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        """
        Create a new User instance based on the validated data.

        Args:
            validated_data (dict): The validated data for creating a new User.

        Returns:
            User: The newly created User instance.

        """
        print(validated_data)
        user = User.objects.create_user(**validated_data)
        return user


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ["id", "title", "content", "created_at", "author"]
        extra_kwargs = {"author": {"read_only": True}}

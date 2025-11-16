from rest_framework import serializers
from django.contrib.auth.models import User
from .models import CustomUserProfile
from .models import CustomUserProfile
from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["username", "email", "password"]

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"]
        )
        CustomUserProfile.objects.create(user=user)
        return user

class CustomUserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUserProfile
        fields = ['first_name', 'last_name', 'phone', 'address', 'city', 'birth_date']

class UserSerializer(serializers.ModelSerializer):
    profile = CustomUserProfileSerializer(source='custom_profile', read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'profile']

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']
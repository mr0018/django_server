from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'first_name', 'last_name', 'gender', 'dob', 'email', 'phone', 'created_on', 'updated_on']

class CustomUserRegistrationSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = CustomUser(**validated_data)
        user.set_password(password)
        user.save()
        return user
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'gender', 'dob', 'email', 'password', 'phone','is_staff', 'is_superuser']

class CustomUserLoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()
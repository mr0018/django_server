from django.core.exceptions import ValidationError
from rest_framework import status
from .models import Employees

def custom_validation(data):
    first_name = data['first_name'].strip()
    last_name = data['last_name'].strip()
    email = data['email'].strip()
    password = data['password'].strip()

    ##
    if not first_name:
        raise ValidationError({"message": "First name is required","status_code":status.HTTP_400_BAD_REQUEST})
    elif len(first_name) < 3:
       raise ValidationError({"message": 'First name must be at least 3 characters',"status_code":status.HTTP_400_BAD_REQUEST})
    ##
    if not last_name:
        raise ValidationError({"message": "Last name is required","status_code":status.HTTP_400_BAD_REQUEST})
    elif len(last_name) < 3:
        raise ValidationError({"message": 'Last name must be at least 3 characters',"status_code":status.HTTP_400_BAD_REQUEST})
    ##
    if not email:
        raise ValidationError({"message": "Email Id  is required","status_code":status.HTTP_400_BAD_REQUEST})
    elif Employees.objects.filter(email=email).exists():
        raise ValidationError({"message":"An employee with this email is already present.","status_code":status.HTTP_409_CONFLICT})
    ##
    if not password or len(password) < 8:
        raise ValidationError({"message":"Choose another password, min 8 characters","status_code":status.HTTP_400_BAD_REQUEST})
    ##
    return data

def validate_email(data):
    email = data['email'].strip()
    if not email:
        raise ValidationError({"message": "Email Id  is required","status_code":status.HTTP_400_BAD_REQUEST})
    return True

def validate_password(data):
    password = data['password'].strip()
    if not password:
        raise ValidationError({"message": "Password is required","status_code":status.HTTP_400_BAD_REQUEST})
    return True
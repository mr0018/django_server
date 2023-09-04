from django.core.exceptions import ValidationError
from rest_framework import status

def custom_validation(data):
    name = data['name'].strip()

    ##
    if not name:
        raise ValidationError({"message": "Name is required","status_code":status.HTTP_400_BAD_REQUEST})
    elif len(name) < 3:
       raise ValidationError({"message": 'Name must be at least 3 characters',"status_code":status.HTTP_400_BAD_REQUEST})
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
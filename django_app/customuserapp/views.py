from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate,login as auth_login
from rest_framework_simplejwt.tokens import RefreshToken

from .models import CustomUser
from .serializers import CustomUserLoginSerializer,CustomUserRegistrationSerializer,CustomUserSerializer

@api_view(['POST'])
def login(request):
    serializer = CustomUserLoginSerializer(data=request.data)
    if serializer.is_valid():
        email = serializer.validated_data['email']
        password = serializer.validated_data['password']
        
        user = authenticate(request, email=email, password=password)
        if user is not None:
            auth_login(request, user)
            refresh = RefreshToken.for_user(user)
            user1 = CustomUser.objects.get(email=email)
            user1 = CustomUserSerializer(user1)
            return Response({'refresh': str(refresh), 'access': str(refresh.access_token),'user':user1.data}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    return Response(str(serializer.errors), status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def register(request):
    try:
        serializer = CustomUserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
from django.urls import path
from .views import login,register

urlpatterns = [
    path('login', login, name='create'),
    path('register', register, name='register'),
]

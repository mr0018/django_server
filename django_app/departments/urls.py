from django.urls import path
from .views import department_create, get_department

urlpatterns = [
    path('create', department_create, name='create'),
    path('list', get_department, name='list'),
]

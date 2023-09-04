from django.urls import path
from .views import employees_list,employee_create

urlpatterns = [
    path('create', employee_create, name='create'),
    path('list', employees_list, name='list'),
]

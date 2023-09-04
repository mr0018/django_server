from rest_framework import serializers
from .models import Employees

class EmployeesSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return Employees.objects.create(**validated_data)
        
    class Meta:
        model = Employees
        fields = ['id', 'first_name', 'last_name', 'gender', 'dob', 'email', 'phone', 'created_on', 'updated_on','department_id']

class GetEmployeesAsHod(serializers.ModelSerializer):
     class Meta:
        model = Employees
        fields = ['id', 'first_name', 'last_name']
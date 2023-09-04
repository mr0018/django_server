from rest_framework import serializers
from .models import Department
from employees.serializers import GetEmployeesAsHod

class DepartmentsSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return Department.objects.create(**validated_data)
        
    class Meta:
        model = Department
        fields = ['id', 'name', 'hod_id','created_on', 'updated_on','description']

class GetDepartmentWithHod(serializers.ModelSerializer):
    hod = GetEmployeesAsHod(source='hod_id')  # Serialize the HOD using the GetEmployeesAsHod

    class Meta:
        model = Department
        fields = '__all__'
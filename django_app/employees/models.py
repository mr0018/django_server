from django.db import models
# from departments.models import Department

class Employees(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=False,blank=False)
    dob = models.DateField(null=False, blank=False)
    email = models.CharField("Employee's email id", unique=True, max_length=120)
    phone = models.CharField(max_length=15, null=False,blank=False)
    created_on = models.DateTimeField("Employee created on date", auto_now_add=True)
    updated_on = models.DateTimeField("Employee updated on date", auto_now=True)
    department_id = models.ForeignKey('departments.Department', db_column='department_id', null=True, on_delete=models.SET_NULL, to_field='id')
    
    def __str__(self):
        return self.email
        
    class Meta:
        db_table = 'employees'

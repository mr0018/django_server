from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=200,null=False,blank=False,unique=True)
    description = models.TextField(max_length=1000,null=True,blank=True)
    hod_id = models.ForeignKey("employees.Employees", on_delete=models.SET_NULL, null=True, blank=True, db_column='hod_id',to_field='id')
    created_on = models.DateTimeField("Department created on date", auto_now_add=True)
    updated_on = models.DateTimeField("Department updated on date", auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'departments'

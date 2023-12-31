# Generated by Django 4.2.4 on 2023-09-04 11:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("employees", "0001_initial"),
        ("departments", "0002_remove_department_hod_id_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="department",
            name="hod_id",
            field=models.ForeignKey(
                blank=True,
                db_column="hod_id",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="employees.employees",
            ),
        ),
    ]

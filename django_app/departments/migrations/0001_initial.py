# Generated by Django 4.2.4 on 2023-09-04 06:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("employees", "__first__"),
    ]

    operations = [
        migrations.CreateModel(
            name="Department",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("description", models.TextField()),
                (
                    "created_on",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Department created on date"
                    ),
                ),
                (
                    "updated_on",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Department updated on date"
                    ),
                ),
                (
                    "hod_id",
                    models.ForeignKey(
                        blank=True,
                        db_column="hod_id",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="employees.employees",
                    ),
                ),
            ],
            options={
                "db_table": "departments",
            },
        ),
    ]
# Generated by Django 4.2.4 on 2023-08-31 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("customuserapp", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="password",
            field=models.CharField(
                max_length=100, unique=True, verbose_name="User's password"
            ),
        ),
    ]

# Generated by Django 5.0.2 on 2024-03-03 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('birthdays', '0002_employee_roles'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='telegram_url',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
# Generated by Django 5.0.2 on 2024-03-03 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('birthdays', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='roles',
            field=models.ManyToManyField(to='birthdays.role'),
        ),
    ]

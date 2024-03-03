from django.apps import AppConfig
import schedule
import time
from django.core.management import call_command


class BirthdaysConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'birthdays'
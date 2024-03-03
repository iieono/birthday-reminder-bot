from django.db import models
import uuid

from django.db.models.signals import post_save


class Role(models.Model):
    role_name = models.CharField(max_length=20)

    def __str__(self):
        return self.role_name

class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField()
    image = models.ImageField(null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False )
    telegram_chat_id = models.CharField(max_length=100, null=True, blank=True)
    roles = models.ManyToManyField(Role)

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.birth_date}"

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"


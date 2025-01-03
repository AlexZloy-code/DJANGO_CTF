# myapp/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    fine = models.IntegerField(default=0)

    def __str__(self):
        return self.username

    def get_id(self):
        return self.id

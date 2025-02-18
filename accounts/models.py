from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    telegram = models.CharField(max_length=50, blank=True)

    class Meta:
        permissions = [
            ("black_list", "В чёрном списке"),
        ]

    def __str__(self):
        return self.username
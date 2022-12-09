from django.contrib.auth.models import AbstractUser
from django.db import models


class Users(AbstractUser):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.get_full_name()
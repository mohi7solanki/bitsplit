from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    bytes = models.IntegerField(default=1)

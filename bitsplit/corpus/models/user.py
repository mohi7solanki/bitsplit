from django.contrib.auth.models import AbstractUser
from django.db import models


def upload_user_profile(instance, filepath):
    return f'profile_pictures/{instance.username}{filepath[filepath.rindex("."):]}'


class User(AbstractUser):
    profile_image = models.ImageField(upload_to=upload_user_profile)

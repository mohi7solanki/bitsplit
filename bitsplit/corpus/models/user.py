from django.contrib.auth.models import AbstractUser
from django.db import models

from .utils import UploadPath


class User(AbstractUser):
    profile_image = models.ImageField(
        upload_to=UploadPath.get_upload_path(
            dir_name='profile_images', field_name='username'
        )
    )

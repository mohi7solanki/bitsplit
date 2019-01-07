import string

from django.contrib.auth import get_user_model
from django.utils.crypto import get_random_string


class UploadPath:
    def __init__(self, dir_name, field_name):
        self.dir_name = dir_name
        self.field_name = field_name

    @classmethod
    def get_upload_path(cls, dir_name, field_name):
        instance = cls(dir_name, field_name)
        return instance._get_file_path

    def _get_file_path(self, instance, filepath):
        ext = filepath[filepath.rindex('.'):]
        name = getattr(instance, self.field_name)
        filename = f'{name}{ext}'
        return f'{self.dir_name}/{filename}'


def get_sentinel_user():
    user, _ = get_user_model().objects.get_or_create(username='deleted')
    return user

def get_unique_slug(instance, length):
    all_chars = string.ascii_letters + string.digits
    model = instance.__class__
    while True:
        slug = get_random_string(length=length, allowed_chars=all_chars)
        if not model._default_manager.filter(slug=slug).exists():
            break
    return slug

from django.contrib.auth import get_user_model


def get_sentinel_user():
    user, _ = get_user_model().objects.get_or_create(username='deleted')
    return user


def get_upload_path(dir_name, field_name):
    def wrap(instance, filepath):
        ext = filepath[filepath.rindex('.'):]
        name = getattr(instance, field_name)
        filename = f'{name}{ext}'
        return f'{dir_name}/{filename}'
    return wrap

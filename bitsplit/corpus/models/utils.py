from django.contrib.auth import get_user_model


def get_sentinel_user():
    user, _ = get_user_model().objects.get_or_create(username='deleted')
    return user

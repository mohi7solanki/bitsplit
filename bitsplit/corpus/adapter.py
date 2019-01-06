from django.contrib.auth import get_user_model
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter


class CustomUsernameAdapter(DefaultSocialAccountAdapter):
    """
    To set username from user's social email while sign up
    If it is available.
    """

    @staticmethod
    def _get_possible_username(email):
        """
        Return username from user's email while social sign-in if the
        username does not exist in the db empty otherwise.
        """
        username = ''
        possible_username = email.split('@')[0]
        model = get_user_model()
        if not model.objects.filter(username=possible_username).exists():
            username = possible_username
        return username

    def populate_user(self, request, sociallogin, data):
        user = super().populate_user(request, sociallogin, data)
        user.username = self._get_possible_username(data['email'])
        return user

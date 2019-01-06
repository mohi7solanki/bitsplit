from django.contrib.auth import get_user_model
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    profile_image = serializers.SerializerMethodField()

    class Meta:
        model = get_user_model()
        fields = (
            'username', 'email', 'first_name', 'last_name', 'profile_image'
        )
        read_only_fields = ('email',)

    def get_profile_image(self, instance):
        if instance.profile_image:
            image_url = instance.profile_image.url
        else:
            social_account = instance.socialaccount_set.last()
            image_url = social_account.extra_data['picture']
        return image_url

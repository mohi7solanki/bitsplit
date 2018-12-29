from rest_framework.serializers import ModelSerializer

from bitsplit.corpus import models


class BitSerializer(ModelSerializer):
    class Meta:
        model = models.Bit
        fields = (
            'title',
            'upvotes',
            'downvotes',
            'creator'
        )

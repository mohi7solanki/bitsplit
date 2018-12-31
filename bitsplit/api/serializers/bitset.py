from rest_framework import serializers

from bitsplit.corpus import models


class BitSetSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'slug',
            'description',
            'moderators',
            'logo',
        )
        model = models.BitSet

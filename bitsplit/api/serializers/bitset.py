from rest_framework import serializers

from bitsplit.corpus import models


class BitSetSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'name',
            'description',
            'moderators',
        )
        model = models.BitSet

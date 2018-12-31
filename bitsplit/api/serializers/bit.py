from rest_framework.serializers import ModelSerializer
from rest_framework import fields

from bitsplit.corpus import models


class BitSerializer(ModelSerializer):
    bitset_logo = fields.ImageField(source='bitset.logo')
    bitset_slug = fields.CharField(source='bitset.slug')
    username = fields.CharField(source='creator.username')
    class Meta:
        model = models.Bit
        fields = (
            'title',
            'bitset_logo',
            'bitset_slug',
            'bit_type',
            'content',
            'upvotes',
            'downvotes',
            'score',
            'username',
        )

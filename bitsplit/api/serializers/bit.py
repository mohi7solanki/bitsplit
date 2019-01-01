from rest_framework import serializers
from rest_framework import fields

from bitsplit.corpus import models


class BitSerializer(serializers.ModelSerializer):
    bitset_logo = fields.ImageField(source='bitset.logo')
    bitset_slug = fields.CharField(source='bitset.slug')
    username = fields.CharField(source='creator.username')
    comments_count = serializers.SerializerMethodField()
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
            'comments_count',
        )

    def get_comments_count(self, instance):
        return instance.comments.count()

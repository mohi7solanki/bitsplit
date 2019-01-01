from rest_framework import serializers

from bitsplit.corpus import models


class RecursiveSerializer(serializers.Serializer):
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class CommentSerializer(serializers.ModelSerializer):
    children = RecursiveSerializer(many=True, read_only=True)

    class Meta:
        model = models.Comment
        fields = ('id', 'updated_at', 'text', 'parent', 'children')

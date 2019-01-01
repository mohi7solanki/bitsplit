from django.conf import settings
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

from .abstract import Votable
from .bit import Bit


class Comment(MPTTModel, Votable):

    # Denormalized fields to reduce query
    author_username = models.CharField(max_length=100)
    author_name = models.CharField(max_length=100)

    text = models.TextField()
    bit = models.ForeignKey(
        Bit, related_name='comments', on_delete=models.CASCADE
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='comments',
        on_delete=models.CASCADE
    )
    parent = TreeForeignKey(
        'self',
        related_name='children',
        null=True,
        blank=True,
        db_index=True,
        on_delete=models.CASCADE,
    )

    class MPTTMeta:
        order_insertion_by = ['updated_at']

    def __str__(self):
        return self.text[:40]

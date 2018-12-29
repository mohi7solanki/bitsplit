from django.db import models
from django.conf import settings

from .base import BaseModel
from .limits import MAX_BITSET_NAME


class BitSet(BaseModel):
    # options one to one field to bitset options
    name = models.CharField(max_length=MAX_BITSET_NAME)
    description = models.TextField()
    moderators = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='bitsets_moderating'
    )

    def __str__(self):
        return f'{self.name}'

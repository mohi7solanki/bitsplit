from django.conf import settings
from django.db import models

from .base import BaseModel
from .bitset import BitSet


class Option(BaseModel):
    PUBLIC = "public"
    RESTRICTED = "restricted"
    PRIVATE = "private"
    BITSET_TYPE_CHOICES = (
        (PUBLIC, 'Public'),
        (RESTRICTED, 'Restricted'),
        (PRIVATE, 'Private'),
    )
    accent_color = models.CharField(
        max_length=7,
        blank=True,
        default=settings.DEFAULT_ACCENT_COLOR
    )
    bitset_type = models.CharField(max_length=20, choices=BITSET_TYPE_CHOICES)
    bit = models.OneToOneField(BitSet, on_delete=models.CASCADE)

    def __str__(self):
        return f'Option : {self.bitset.slug}'

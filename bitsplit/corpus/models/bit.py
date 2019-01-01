from django.conf import settings
from django.db import models

from .abstract import Votable
from .bitset import BitSet
from .limits import MAX_TITLE_LENGTH
from .utils import get_sentinel_user


class Bit(Votable):
    BIT_CHOICES = (
        ('url', 'URL'),
        ('txt', 'Text'),
        ('img', 'Image')
    )
    title = models.CharField(max_length=MAX_TITLE_LENGTH)
    url = models.URLField(null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    bit_type = models.CharField(max_length=3, choices=BIT_CHOICES)
    bitset = models.ForeignKey(
        BitSet, on_delete=models.CASCADE, related_name='bits'
    )
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='bits',
        on_delete=models.SET(get_sentinel_user),
    )
    users_bookmarked = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='bookmarked_bits',
        blank=True,
    )

    @property
    def content(self):
        if self.bit_type == 'img':
            return self.image.url
        if self.bit_type == 'txt':
            return self.text
        return self.url

    def __str__(self):
        return self.title

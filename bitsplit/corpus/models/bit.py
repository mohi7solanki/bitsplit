from django.conf import settings
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models

from corpus.vote import Vote
from .base import BaseModel
from .limits import MAX_TITLE_LENGTH
from .utils import get_sentinel_user


class Bit(BaseModel):
    BIT_CHOICES = (
        ('url', 'URL'),
        ('txt', 'text'),
    )
    title = models.CharField(max_length=MAX_TITLE_LENGTH)
    upvotes = models.PositiveIntegerField(default=0)
    downvotes = models.PositiveIntegerField(default=0)
    url = models.URLField(null=True, blank=True)
    text = models.TextField(blank=True)
    bit_type = models.CharField(max_length=3, choices=BIT_CHOICES)
    votes = GenericRelation(Vote, related_query_name='bits')
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='bits',
        on_delete=models.SET(get_sentinel_user),
    )
    # TO DO: foreign key to community

    @property
    def score(self):
        return self.upvotes - self.downvotes

    def __str__(self):
        return self.title[:7]

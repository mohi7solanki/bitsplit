from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

from corpus.models import Bit
from .base import BaseModel


class Vote(BaseModel):
    _CANCEL_VOTE = 0
    UPVOTE = 1
    DOWNVOTE = 2

    value = models.PositiveIntegerField(default=0)
    bit = models.ForeignKey(Bit, related_name='votes', on_delete=models.CASCADE)
    voter = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='votes',
        on_delete=models.CASCADE,
    )
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

    class Meta:
        unique_together = ('bit', 'voter')

    def cast_vote(self, action):
        self.value = self._CANCEL_VOTE if action == self.value else action
        self.save()

    def __str__(self):
        vote_map = {0: 'No Vote', 1: 'Upvote', 2: 'Downvote'}
        return vote_map[self.value]

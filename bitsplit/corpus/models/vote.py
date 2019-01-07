from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

from .base import BaseModel


class VoteManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().exclude(value=self.model._CANCEL_VOTE)


class Vote(BaseModel):
    _CANCEL_VOTE = 0
    UPVOTE = 1
    DOWNVOTE = 2

    slug = models.SlugField(max_length=8, unique=True)
    value = models.PositiveIntegerField(default=0)
    voter = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='votes',
        on_delete=models.CASCADE,
    )
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

    objects = VoteManager()
    _create = models.Manager()

    class Meta:
        unique_together = ('content_type', 'object_id', 'voter')
        index_together = (('content_type', 'object_id'),)

    def cast_vote(self, action):
        """
        If the action is same as the current vote's action then it
        will store the value as 0 which will be considered as deleted.
        """
        self.value = self._CANCEL_VOTE if action == self.value else action
        self.save()
        return self.value == self._CANCEL_VOTE  # deleted

    def __str__(self):
        vote_map = {1: 'Upvote', 2: 'Downvote'}
        return vote_map[self.value]

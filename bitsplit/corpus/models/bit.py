from django.conf import settings
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.db.models import F


from .base import BaseModel
from .bitset import BitSet
from .limits import MAX_TITLE_LENGTH
from .utils import get_sentinel_user
from .vote import Vote


class Bit(BaseModel):
    BIT_CHOICES = (
        ('url', 'URL'),
        ('txt', 'text'),
        ('img', 'image')
    )
    title = models.CharField(max_length=MAX_TITLE_LENGTH)
    upvotes = models.PositiveIntegerField(default=0)
    downvotes = models.PositiveIntegerField(default=0)
    url = models.URLField(null=True, blank=True)
    text = models.TextField(blank=True)
    image = models.ImageField()
    bit_type = models.CharField(max_length=3, choices=BIT_CHOICES)
    bitset = models.ForeignKey(
        BitSet, on_delete=models.CASCADE, related_name='bits'
    )
    votes = GenericRelation(Vote, related_query_name='bits')
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='bits',
        on_delete=models.SET(get_sentinel_user),
    )
    users_bookmarked = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='bookmarked_bits',
    )

    @property
    def score(self):
        return self.upvotes - self.downvotes

    def _vote(self, voter, value, field):
        # pylint: disable=E1102
        vote, created = self.votes(manager='_create').get_or_create(voter=voter)
        deleted = vote.cast_vote(value)
        if created or not deleted:
            setattr(self, field, F(field) + 1)
        else:
            setattr(self, field, F(field) - 1)
        self.save()

    def upvote(self, voter):
        self._vote(voter=voter, value=Vote.UPVOTE, field='upvotes')

    def downvote(self, voter):
        self._vote(voter=voter, value=Vote.DOWNVOTE, field='downvotes')

    def __str__(self):
        return self.title

from django.db import models
from django.db.models import F
from django.contrib.contenttypes.fields import GenericRelation

from .base import BaseModel
from .vote import Vote


class Votable(BaseModel):
    """
    Abstract class that can be inherited from to make
    concrete class Votable.
    """

    # Denormalized fields to reduce query.
    upvotes = models.PositiveIntegerField(default=0)
    downvotes = models.PositiveIntegerField(default=0)

    votes = GenericRelation(Vote, related_query_name='%(class)s')

    class Meta:
        abstract = True

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

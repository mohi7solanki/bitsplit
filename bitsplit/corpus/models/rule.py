from django.db import models

from .base import BaseModel
from .bit import BitSet


class Rule(BaseModel):
    POSTS_AND_COMMENTS = 1
    POSTS_ONLY = 2
    COMMENTS_ONLY = 3
    APPLIES_TO_CHOICE = (
        (POSTS_AND_COMMENTS, 'Posts and comments'),
        (POSTS_ONLY, 'Posts'),
        (COMMENTS_ONLY, 'Comments only'),
    )
    slug = models.SlugField(max_length=8, unique=True)
    name = models.CharField(max_length=50)
    applies_to = models.IntegerField(choices=APPLIES_TO_CHOICE)
    violation_reason = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    bitset = models.ForeignKey(
        BitSet,
        on_delete=models.CASCADE,
        related_name='rules'
    )

    def __str__(self):
        return self.name

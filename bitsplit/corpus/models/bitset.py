from django.db import models
from django.conf import settings

from .base import BaseModel
from .limits import MAX_BITSET_NAME
from .utils import UploadPath


class BitSet(BaseModel):
    name = models.CharField(max_length=MAX_BITSET_NAME)
    slug = models.SlugField(max_length=MAX_BITSET_NAME, unique=True)
    description = models.TextField()
    logo = models.ImageField(
        upload_to=UploadPath.get_upload_path(
            dir_name='bitset_logos', field_name='slug'
        )
    )
    moderators = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='bitsets_moderating'
    )
    banned_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='bitsets_banned',
        blank=True
    )
    muted_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='bitsets_muted',
        blank=True
    )
    approved_submitters = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='bitsets_approved_submitted',
        blank=True
    )
    option = models.OneToOneField(
        'Option',
        null=True,
        on_delete=models.SET_NULL
        )

    class Meta:
        verbose_name_plural = 'BitSets'

    def __str__(self):
        return f'{self.slug}'


class Option(models.Model):
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

    def __str__(self):
        if hasattr(self, 'bitset'):
            return f'Option : {self.bitset}'
        else:
            return str(self.id)


class Rule(BaseModel):
    POSTS_AND_COMMENTS = 1
    POSTS_ONLY = 2
    COMMENTS_ONLY = 3
    APPLIES_TO_CHOICE = (
        (POSTS_AND_COMMENTS, 'Posts and comments'),
        (POSTS_ONLY, 'Posts'),
        (COMMENTS_ONLY, 'Comments only'),
    )
    name = models.CharField(max_length=50)
    applies_to = models.IntegerField(choices=APPLIES_TO_CHOICE)
    voilation_reason = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    bitset = models.ForeignKey(BitSet, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

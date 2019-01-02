from django.db import models
from django.conf import settings

from .base import BaseModel
from .limits import MAX_BITSET_NAME
from .utils import UploadPath


class BitSet(BaseModel):
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
        related_name='bitsets_banned_in',
        blank=True
    )
    muted_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='bitsets_muted_in',
        blank=True
    )
    approved_submitters = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='bitsets_approved_in',
        blank=True
    )

    class Meta:
        verbose_name_plural = 'BitSets'

    def __str__(self):
        return self.slug

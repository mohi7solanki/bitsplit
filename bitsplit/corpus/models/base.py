from django.db import models

from .utils import get_unique_slug

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if self.slug is None:
            slug_length = self._meta.get_field('slug').max_length
            self.slug = get_unique_slug(self, slug_length)
        super().save(*args, **kwargs)

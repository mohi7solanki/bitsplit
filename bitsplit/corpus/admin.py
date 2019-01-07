from django.contrib import admin

from bitsplit.corpus import models

admin.site.register(models.Bit)
admin.site.register(models.User)
admin.site.register(models.BitSet)
admin.site.register(models.Option)
admin.site.register(models.Rule)

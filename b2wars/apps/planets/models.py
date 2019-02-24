from django.db import models
from django.utils.text import gettext_lazy as _

from b2wars.apps.core.mixins.models import TimeStampedMixin


class Planet(TimeStampedMixin):

    name = models.CharField(_('Name'), max_length=255, unique=True)
    climate = models.CharField(_('Climate'), max_length=255)
    terrain = models.CharField(_('Terrain'), max_length=255)

    def __str__(self):
        return self.name

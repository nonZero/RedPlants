from django.conf import settings
from django.db import models
from plants.models import Specie


class Observation(models.Model):
    specie = models.ForeignKey(Specie, related_name='obs')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='obs')
    created_at = models.DateTimeField(auto_now_add=True)
    recorded_at = models.DateField(null=True, blank=True)
    lat = models.FloatField()
    lon = models.FloatField()

from __future__ import unicode_literals

from django.db import models

class Noise(models.Model):
	dong = models.PositiveSmallIntegerField()
	ho = models.PositiveSmallIntegerField()
	noise_data = models.FloatField()

# Create your models here.

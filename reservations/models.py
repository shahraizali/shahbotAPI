# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class RoomReservation(models.Model):
    amenities = models.CharField(max_length=200, null=True, blank=True)
    bed_size = models.CharField(max_length=200, null=True, blank=True)
    date = models.CharField(max_length=200, null=True, blank=True)
    occupants = models.CharField(max_length=200, null=True, blank=True)
    days_to_stay = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'RoomReservations'
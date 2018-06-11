# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from rest_framework import status, viewsets
from .serializers import RoomReservationSerializer
from .models import RoomReservation

class ReservationView(viewsets.ModelViewSet):
    queryset = RoomReservation.objects.all()
    serializer_class = RoomReservationSerializer

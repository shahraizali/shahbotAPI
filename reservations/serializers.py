from rest_framework import serializers

from .models import RoomReservation

class RoomReservationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RoomReservation
        fields = ('id', 'amenities', 'bed_size', 'date', 'occupants', 'days_to_stay')
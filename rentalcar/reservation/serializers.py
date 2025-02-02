from .models import Reservation
from rest_framework import serializers


class ReservationSerializers(serializers.ModelSerializer):
    class Meta:
        model=Reservation
        fields='__all__'
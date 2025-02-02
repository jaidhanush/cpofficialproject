from .models import Reservation
from .serializers import ReservationSerializers
from rest_framework import viewsets

class ReservationViewSet(viewsets.ModelViewSet):
    queryset=Reservation.objects.all()
    serializer_class=ReservationSerializers


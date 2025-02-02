from rest_framework import viewsets
from .models import Booking
from .serializers import BookingSerializers


class BookingViewSet(viewsets.ModelViewSet):
    queryset=Booking.objects.all()
    serializer_class=BookingSerializers

from rest_framework import viewsets
from .models import Cancellation
from .serializers import CancellationSerializers

class CancellationViewSet(viewsets.ModelViewSet):
    queryset=Cancellation.objects.all()
    serializer_class=CancellationSerializers

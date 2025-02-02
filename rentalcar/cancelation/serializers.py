from rest_framework import serializers
from .models import Cancellation

class CancellationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cancellation
        fields = '__all__'
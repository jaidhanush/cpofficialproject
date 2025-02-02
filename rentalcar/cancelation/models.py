from django.db import models
from booking.models import Booking

class Cancellation(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    cancellation_date = models.DateTimeField(auto_now_add=True)
    reason = models.TextField()

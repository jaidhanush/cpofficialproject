from django.db import models
from car.models import Car

class Booking(models.Model):
    # User =models.ForeignKey(User,on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)
    pickup_date = models.DateTimeField()
    return_date = models.DateTimeField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
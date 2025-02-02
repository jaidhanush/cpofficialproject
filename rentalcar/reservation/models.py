from django.db import models
from car.models import Car

class Reservation(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    reservation_date = models.DateTimeField(auto_now_add=True)
    pickup_date = models.DateTimeField()
    return_date = models.DateTimeField()
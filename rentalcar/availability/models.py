from django.db import models
from car.models import Car


class Availability(models.Model):
    car = models.OneToOneField(Car, on_delete=models.CASCADE)
    pickup_date = models.DateTimeField()
    return_date = models.DateTimeField()
    available_quantity = models.IntegerField()
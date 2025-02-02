from django.db import models

class Car(models.Model) :
    brand=models.CharField(max_length=40)
    model=models.CharField(max_length=40)
    year=models.IntegerField
    license_plate=models.CharField(max_length=40)
    availability_status=models.BooleanField(default=True)
    

#MyApp/models.py
from email.policy import default
from django.db import models
from django.contrib.auth.models import User  # Import the User model
from django.urls import reverse

class Car(models.Model):
    car_id = models.IntegerField(default=0)
    car_name = models.CharField(max_length=30, default="")
    car_desc = models.CharField(max_length=300, default="")
    vehicle_type = models.CharField(max_length=50, default="car")  # Default value added here
    max_persons = models.IntegerField(default=4)
    fuel_efficiency = models.FloatField(default=10.0)
    price_per_km = models.DecimalField(max_digits=10, decimal_places=2, default=12.89)
    availability = models.BooleanField(default=True)
    image_url = models.CharField(max_length=200, default='car.jpg')

    def __str__(self):
        return self.car_name

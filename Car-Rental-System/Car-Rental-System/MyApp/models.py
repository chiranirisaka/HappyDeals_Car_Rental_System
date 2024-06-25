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

class Booking(models.Model):
    vehicle = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='bookings')
    customer_name = models.CharField(max_length=30, default="")
    customer_phone = models.CharField(max_length=15, default="")
    nic = models.CharField(max_length=20, default="")  # New field for NIC
    pickup_date = models.DateField()
    return_date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.vehicle.car_name} - {self.pickup_date} to {self.return_date}"

    def save(self, *args, **kwargs):
        # Check for overlapping bookings
        overlapping_bookings = Booking.objects.filter(vehicle=self.vehicle).filter(
            models.Q(pickup_date__range=[self.pickup_date, self.return_date]) |
            models.Q(return_date__range=[self.pickup_date, self.return_date])
        ).exclude(pk=self.pk)
        if overlapping_bookings.exists():
            raise ValueError("This vehicle is already booked for the given dates.")

        super().save(*args, **kwargs)


class Contact(models.Model):
    message = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150,default="")
    email = models.CharField(max_length=150,default="")
    phone_number = models.CharField(max_length=15,default="")
    message = models.TextField(max_length=500,default="")

    def __str__(self) :
        return self.name


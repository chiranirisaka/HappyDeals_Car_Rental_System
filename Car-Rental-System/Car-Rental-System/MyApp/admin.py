#MyApp/admin.py
from django.contrib import admin
from .models import Car,Booking,Contact

admin.site.register(Car)
admin.site.register(Booking)
admin.site.register(Contact)



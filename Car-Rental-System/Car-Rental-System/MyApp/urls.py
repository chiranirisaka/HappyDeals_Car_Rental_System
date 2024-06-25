#MyApp/urls.py
# from django.contrib import admin
from django.urls import path
from MyApp import views

urlpatterns = [
    path("", views.index, name='home'),
    path("home", views.index, name='home'),

    path("about", views.about, name='about'),
    path("vehicles", views.vehicles, name='vehicles'),
    path("register", views.register, name="register"),
    path("signin", views.signin, name="signin"),
    path("signout", views.signout, name="signout"),
    path('rent/<int:vehicle_id>/', views.rent_vehicle, name='rent_vehicle'),
    path('booking_history/', views.booking_history, name='booking_history'),
path('delete_booking/<int:booking_id>/', views.delete_booking, name='delete_booking'),  # URL for delete booking
    path("contact", views.contact, name='contact'),
    # path("vehicles",views.Order,name = 'vehicles'),
    # path("bike",views.bike,name = 'bike'),
    # path("bus",views.bus,name = 'bus'),
    
    # path("bill", views.bill, name="bill"),

    ]
    

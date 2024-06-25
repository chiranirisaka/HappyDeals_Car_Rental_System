#MyApp/views.py

# from email.mime import message
# from pyexpat import model
from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import Car, Booking, Contact
from datetime import datetime



@login_required
def booking_history(request):
    bookings = Booking.objects.filter(customer_name=request.user.username)
    return render(request, 'booking_history.html', {'bookings': bookings})

@login_required
def delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    if request.method == 'POST' and request.user.username == booking.customer_name:
        booking.delete()
    return redirect('booking_history')  # Redirect to the booking history page


def index(request):
	return render(request,'index.html')

def about(request):
    return render(request,'about.html ')

def register(request):
    if request.method == "POST":
        name = request.POST['name']
        username = request.POST['username']
        number = request.POST['number']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if User.objects.filter(username = username).first():
            messages.error(request,"Username already taken")
            return redirect('register')
        if User.objects.filter(email = email).first():
            messages.error(request,"Email already taken")
            return redirect('register')

        if password != password2:
            messages.error(request,"Passwords do not match")
            return redirect('register')

        myuser = User.objects.create_user(username=username,email=email,password=password)
        myuser.name = name
        myuser.save()



        messages.success(request,"Your account has been successfully created!")
        return redirect('signin')


    else:
        print("error")
        return render(request,'register.html')
    

def signin(request):
    if request.method == "POST":
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(username = loginusername,password = loginpassword)
        if user is not None:
            login(request, user)
            # messages.success(request,"Successfully logged in!")
            return redirect('vehicles')
        else:
            messages.error(request,"Invalid credentials")
            return redirect('signin')

    else:
        print("error")
        return render(request,'login.html')

def signout(request):
        logout(request)
        # messages.success(request,"Successfully logged out!")
        return redirect('home')
    
    # return HttpResponse('signout')

def vehicles(request):
    cars = Car.objects.all()
    # print(cars)
    params = {'car':cars}
    return render(request,'vehicles.html ',params)


@login_required
def rent_vehicle(request, vehicle_id):
    vehicle = Car.objects.get(pk=vehicle_id)

    if request.method == 'POST':
        customer_name = request.POST.get('customerName')
        customer_phone = request.POST.get('customerPhone')
        nic = request.POST.get('nic')  # Retrieve NIC from POST data
        pickup_date = datetime.strptime(request.POST.get('pickupDate'), '%Y-%m-%d').date()
        return_date = datetime.strptime(request.POST.get('returnDate'), '%Y-%m-%d').date()

        try:
            new_booking = Booking(
                vehicle=vehicle,
                customer_name=customer_name,
                customer_phone=customer_phone,
                nic=nic,
                pickup_date=pickup_date,
                return_date=return_date,
                user=request.user
            )
            new_booking.save()
            messages.success(request, f"Booking successful for {vehicle.car_name} from {pickup_date} to {return_date}.")
            return render(request, 'bill.html', {'vehicle': vehicle})

        except ValueError as e:
            messages.error(request, str(e))

    return render(request, 'bill.html', {'vehicle': vehicle})

def contact(request):
    if request.method == "POST":
        contactname = request.POST.get('contactname','')
        contactemail = request.POST.get('contactemail','')
        contactnumber = request.POST.get('contactnumber','')
        contactmsg = request.POST.get('contactmsg','')

        contact = Contact(name = contactname, email = contactemail, phone_number = contactnumber,message = contactmsg)
        contact.save()
    return render(request,'contact.html ')



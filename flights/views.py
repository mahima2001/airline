from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Flight,Passenger
# Create your views here.
def index(request):
    return render(request,'flights/index.html',
    {
        'flights':Flight.objects.all()
    })

def flight(request,flight_id):
    flight=Flight.objects.get(pk=flight_id)#pk-primary key, could also use id instead of pk
    return render(request,'flights/flight.html',{
        'flight':flight,
        'passengers':flight.passenger.all(),
        "non_passengers":Passenger.objects.exclude(flights=flight).all()# means give name of all those people who are not on this flight
    })
 
def book(request,flight_id):
    if request.method=='POST':
        flight=Flight.objects.get(pk=flight_id)
        passenger=Passenger.objects.get(pk= int(request.POST["passenger"]))
        passenger.flights.add(flight)#take this passenger, take this flight and go ahead and this flight to his set of flights
        return HttpResponseRedirect(reverse('flight',args=(flight.id,)))# reverse takes the name and gives us the url
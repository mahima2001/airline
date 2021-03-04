from django.db import models

# Create your models here.

class Airports(models.Model):
    code=models.CharField(max_length=3)
    city=models.CharField(max_length=64)
    def __str__(self):
        return f"{self.city} ({self.code})"
class Flight(models.Model):
    origin=models.ForeignKey(Airports,on_delete=models.CASCADE,related_name="departure")
    destination=models.ForeignKey(Airports,on_delete=models.CASCADE,related_name="arrivals")
    duration=models.IntegerField()

    def __str__(self):
        return f"{self.id}:{self.origin} to {self.destination}"# String representation of our object

class Passenger(models.Model):
    first=models.CharField(max_length=64)
    last=models.CharField(max_length=64)
    flights=models.ManyToManyField(Flight,blank=True,related_name='passenger')# many passenger could be in one flight;one passenger could be in many flight;blank=True->Could not be any flight
    def __str__(self):
        return f"{self.first} {self.last}"
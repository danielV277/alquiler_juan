from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.urls import reverse
from django.core.validators import MinLengthValidator, MaxLengthValidator
# Create your models here.

class User(models.Model):
    numId = models.CharField(max_length=11)
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    birth_date = models.DateField()
    email = models.EmailField()
    phone_number = models.CharField(max_length=10)
    photo = models.ImageField(upload_to='user_photo/')
    
class Vehicle(models.Model):
    brand = models.CharField(max_length=80)
    model = models.CharField(max_length=80)
    type = models.CharField(max_length=80)
    year = models.IntegerField(validators=[MinLengthValidator(1900), MaxLengthValidator(2025)])
    plates = models.CharField(max_length=10)
    state = models.CharField(max_length=10)
    cost_per_day = models.DecimalField(max_digits=10,decimal_places=2)
    photo = models.ImageField(upload_to='vehicle_photo/')

class Request(models.Model):
    user_id =  models.ForeignKey('User', on_delete=models.PROTECT, related_name='get_requests')
    vehicle_id = models.ForeignKey('Vehicle', on_delete=models.PROTECT, related_name= 'get_requests')
    request_date = models.DateField()
    request_days = models.IntegerField()
    expected_return_date = models.DateField()
    departure_date = models.DateField()
    entry_date = models.DateField()
    request_status = models.CharField(max_length=80)
    total_cost = models.DecimalField(max_digits=10,decimal_places=2)
    payment_status = models.CharField(max_length=80)
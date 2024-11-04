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
    
    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
    
    def get_absolute_url(self):
        return reverse("user_list")
    
        
    
class Vehicle(models.Model):
    vehicle_type_choises = [
        ('car', 'Car'),
        ('motorcycle', 'Motorcycle'),
        ('truck', 'Truck'),
    ]
    
    Vehicle_state_choises =[
        ('available','Available'),
        ('requested','Requested'),
        ('rented','Rented')
    ]
    
    # validators=[MinLengthValidator(1900), MaxLengthValidator(2025)]
    brand = models.CharField(max_length=80)
    model = models.CharField(max_length=80)
    type = models.CharField(max_length=80, choices=vehicle_type_choises)
    year = models.IntegerField()
    plates = models.CharField(max_length=10)
    state = models.CharField(max_length=50, choices=Vehicle_state_choises)
    cost_per_day = models.DecimalField(max_digits=10,decimal_places=2)
    photo = models.ImageField(upload_to='vehicle_photo/')

    @property
    def full_name(self):
        return f'{self.type.capitalize()} {self.model} {self.brand} {self.year}'

    def get_absolute_url(self):
        return reverse("vehicle_list")
 


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
    

    
@receiver(post_delete, sender=User)
def team_delete(sender, instance, **kwargs):
    """ Borra los ficheros de las fotos que se eliminan. """
    instance.photo.delete(False)


@receiver(post_delete, sender=Vehicle)
def team_delete(sender, instance, **kwargs):
    """ Borra los ficheros de las fotos que se eliminan. """
    instance.photo.delete(False)
    
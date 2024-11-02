from django.shortcuts import render
from django.views.generic import ListView,CreateView
from alquiler.models import Vehicle, User
from .forms import VehicleForm

# Create your views here.

class VehicleList(ListView):
    model = Vehicle
    
    
    
class VehicleAdd(CreateView):
    model = Vehicle
    form_class = VehicleForm
    success_url = '/vehicle/list'
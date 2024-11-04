from django.shortcuts import render
from django.views.generic import ListView,CreateView,DetailView,UpdateView, DeleteView
from alquiler.models import Vehicle, User
from .forms import VehicleForm, UserForm
from django.urls import reverse_lazy
# Create your views here.

class VehicleDetail(DetailView):
    model = Vehicle
    

class VehicleList(ListView):
    model = Vehicle
    
    
    
class VehicleAdd(CreateView):
    model = Vehicle
    form_class = VehicleForm
    success_url = '/vehicle/list'
    
class VehicleUpdate(UpdateView):
    model = Vehicle
    form_class = VehicleForm
    
class VehicleDelete(DeleteView):
    model = Vehicle
    success_url = reverse_lazy('vehicle_list')

# USUARIO

class UserAdd(CreateView):
    model = User
    form_class = UserForm
    success_url = '/user/list'
    
class UserList(ListView):
    model = User
    
class UserDelete(DeleteView):
    model = User
    success_url = reverse_lazy('user_list')

class UserUpdate(UpdateView):
    model = User
    form_class = UserForm
    success_url = '/user/list'
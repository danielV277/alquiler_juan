from datetime import timedelta
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView,CreateView,DetailView,UpdateView, DeleteView
from alquiler.models import Request, Vehicle, User
from .forms import VehicleForm, UserForm, VehicleRequestForm
from django.urls import reverse_lazy
# Create your views here.

class VehicleDetail(DetailView):
    model = Vehicle
    

class VehicleList(ListView):
    model = Vehicle
    template_name = 'alquiler/vehicle_list.html'

class VehicleAdd(CreateView):
    model = Vehicle
    form_class = VehicleForm
    success_url = '/vehicle/list'
    
class VehicleUpdate(UpdateView):
    model = Vehicle
    form_class = VehicleForm
    template_name = 'alquiler/vehicle_update.html'  # Asegúrate de que el nombre de plantilla sea correcto
    success_url = reverse_lazy('vehicle_list')

    def form_valid(self, form):
        # Agregar un mensaje de éxito
        messages.success(self.request, 'Vehicle updated successfully!')
        return super().form_valid(form)
    
class VehicleDelete(DeleteView):
    model = Vehicle
    success_url = reverse_lazy('vehicle_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Vehicle deleted successfully!')
        return super().delete(request, *args, **kwargs)

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

class VehicleRequestList(ListView):
    model = Vehicle
    template_name = 'alquiler/vehicle_request_list.html'
    context_object_name = 'available_vehicles'

    def get_queryset(self):
        # Filtrar solo vehículos con estado 'available'
        return Vehicle.objects.filter(state='available')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = VehicleRequestForm()  # Pasar el formulario a la plantilla
        return context
    
class VehicleRequestCreate(CreateView):
    model = Request
    form_class = VehicleRequestForm
    template_name = 'alquiler/request_form.html'
    success_url = reverse_lazy('vehicle_request_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Obtener el vehículo utilizando el parámetro de la URL
        vehicle_id = self.kwargs.get('vehicle_id')
        context['vehicle'] = get_object_or_404(Vehicle, id=vehicle_id)
        
        return context

    def form_valid(self, form):
        request_instance = form.save(commit=False)
        request_instance.user = self.request.user
        request_instance.vehicle = get_object_or_404(Vehicle, id=self.kwargs['vehicle_id'])
        request_instance.expected_return_date = request_instance.request_date + timedelta(days=request_instance.request_days)
        vehicle_cost = request_instance.vehicle.cost_per_day
        request_instance.total_cost = vehicle_cost * request_instance.request_days
        request_instance.request_status = 'Pending'
        request_instance.payment_status = 'Unpaid'
        messages.success(self.request, '¡Solicitud creada con éxito!')
        return super().form_valid(form)
    
def vehicle_request_create(request, pk):
    vehicle = get_object_or_404(Vehicle, pk=pk)

    if request.method == 'POST':
        form = VehicleRequestForm(request.POST)
        if form.is_valid():
            # Asignar el vehículo y el usuario automáticamente
            vehicle_request = form.save(commit=False)
            vehicle_request.vehicle = vehicle
            vehicle_request.user = request.user
            vehicle_request.save()
            return redirect('request_success')  # Redirigir a una página de éxito

    else:
        form = VehicleRequestForm()

    return render(request, 'alquiler/request_form.html', {'form': form, 'vehicle': vehicle})
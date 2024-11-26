from django.shortcuts import render,get_object_or_404, redirect
from django.views.generic import ListView,CreateView,DetailView,UpdateView, DeleteView,View
from alquiler.models import Vehicle, User, Request
from .forms import VehicleForm, UserForm, RequestForm
from django.urls import reverse_lazy, reverse
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

class VehicleUpdateState(View):
    def get(self, request, pk, *args, **kwargs):
        # Obtiene la instancia del objeto
        request_instance = get_object_or_404(Vehicle, pk=pk)

        # Alterna el estado de pago
        request_instance.state = 'available' if request_instance.state == 'rented' else 'rented'
        request_instance.save()

        # Redirige a la página de detalle del vehículo
        return redirect(reverse('vehicle_detail', kwargs={'pk': request_instance.pk}))



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
    
#Request

class RequestAdd(CreateView):
    model = Request
    form_class = RequestForm
    success_url = '/requests/list'
    
    def get_initial(self):
        initial = super().get_initial()
        # Verifica si se proporciona un `pk` en la URL
        vehicle_pk = self.kwargs.get('pk')
        if vehicle_pk:
            # Intenta obtener el vehículo; lanza un 404 si no existe
            get_object_or_404(Vehicle, pk=vehicle_pk)
            initial['vehicle_id'] = vehicle_pk
        return initial
    
    def form_valid(self, form):
        
        response = super().form_valid(form)
        
        vehicle = form.cleaned_data['vehicle_id']
        
        # Cambia el estado del vehículo a 'requested' (o cualquier estado que indique que no está disponible)
        vehicle.state = 'rented'  # Cambia el estado según lo que necesites
        vehicle.save()
        # Redirige al detalle del vehículo (puedes personalizar la URL aquí)
        return redirect('vehicle_detail', pk=vehicle.pk)

    
class RequestList(ListView):
    model = Request
    
class RequestUpdatePaid(View):
   def get(self, request, pk, *args, **kwargs):
        # Obtiene la instancia del objeto
        request_instance = get_object_or_404(Request, pk=pk)

        # Alterna el estado de pago
        request_instance.payment_status = 'paid' if request_instance.payment_status == 'noPaid' else 'noPaid'
        request_instance.save()

        # Redirige a la lista de solicitudes
        return redirect('request_list')
    

    
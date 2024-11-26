from django import forms
from .models import Vehicle,User,Request

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['brand', 'model', 'type', 'year', 'plates', 'state', 'cost_per_day', 'photo']
        widgets = {
            'brand': forms.TextInput(attrs={'class': 'form-control rounded-3'}),
            'model': forms.TextInput(attrs={'class': 'form-control rounded-3'}),
            'type': forms.Select(attrs={'class': 'form-select rounded-3'}),
            'year': forms.NumberInput(attrs={'class': 'form-control rounded-3'}),
            'plates': forms.TextInput(attrs={'class': 'form-control rounded-3'}),
            'state': forms.Select(attrs={'class': 'form-select rounded-3'}),
            'cost_per_day': forms.NumberInput(attrs={'class': 'form-control rounded-3'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control rounded-3'}),
        }

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['numId','first_name','last_name','birth_date','email','phone_number','photo']
        widgets ={
            'numId': forms.TextInput(attrs={'class': 'form-control rounded-3'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control rounded-3'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control rounded-3',}),
            'birth_date': forms.DateInput(attrs={'class': 'form-control rounded-3','type':'date'}),
            'email': forms.EmailInput(attrs={'class': 'form-control rounded-3', 'type':'email'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control rounded-3','minlength':10 }),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control rounded-3'}),
            
        }
        
class RequestForm(forms.ModelForm):
    
    class Meta:
        model = Request
        fields = ['vehicle_id','user_id','request_date','request_days','expected_return_date','departure_date','entry_date','request_status','total_cost','payment_status'] 
        widgets = {
            'vehicle_id': forms.Select(attrs={'class': 'form-select rounded-3'}),
            'user_id': forms.Select(attrs={'class': 'form-select rounded-3'}),
            'request_date': forms.DateInput(attrs={'class': 'form-control rounded-3','type':'date'}),
            'request_days': forms.NumberInput(attrs={'class': 'form-control rounded-3'}),
            'departure_date': forms.DateInput(attrs={'class': 'form-control rounded-3','type':'date'}),
            'expected_return_date': forms.DateInput(attrs={'class': 'form-control rounded-3','type':'date'}),
            'entry_date': forms.DateInput(attrs={'class': 'form-control rounded-3','type':'date'}),
            'request_status': forms.Select(attrs={'class': 'form-select rounded-3'}),
            'total_cost': forms.NumberInput(attrs={'class': 'form-control rounded-3'}),
            'payment_status' : forms.Select(attrs={'class': 'form-select rounded-3'}),
        }
        
    
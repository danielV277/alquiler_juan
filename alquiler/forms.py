from django import forms
from .models import Vehicle

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['brand', 'model', 'type', 'year', 'plates', 'state', 'cost_per_day', 'photo']
        widgets = {
            'brand': forms.TextInput(attrs={'class': 'form-control rounded-3'}),
            'model': forms.TextInput(attrs={'class': 'form-control rounded-3'}),
            'type': forms.TextInput(attrs={'class': 'form-control rounded-3'}),
            'year': forms.NumberInput(attrs={'class': 'form-control rounded-3'}),
            'plates': forms.TextInput(attrs={'class': 'form-control rounded-3'}),
            'state': forms.TextInput(attrs={'class': 'form-control rounded-3'}),
            'cost_per_day': forms.NumberInput(attrs={'class': 'form-control rounded-3'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control rounded-3'}),
        }
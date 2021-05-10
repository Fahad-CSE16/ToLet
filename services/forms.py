from django import forms
from .models import VehicleServe
class VehicleForm(forms.ModelForm):
    TYPE_CHOICE = [
        ('Long Vehicle', 'Long Vehicle'),
        ('Pickup', 'Pickup'),
        ('Truck', 'Truck'),
        ('Van', 'Van'),
    ]
    vehicle_type = forms.ChoiceField(
        required=False,
        choices=TYPE_CHOICE,
    )
    class Meta:
        
        model=VehicleServe
        exclude=['user',]
        
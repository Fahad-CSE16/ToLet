from django import forms
from .models import VehicleServe
class VehicleForm(forms.ModelForm):
    class Meta:
        model=VehicleServe
        exclude=['user',]
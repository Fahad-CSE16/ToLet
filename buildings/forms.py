from django import forms
from .models import Flat,FlatImages
class FlatForm(forms.ModelForm):
    class Meta:
        model=Flat
        exclude=['timestamp','user',]

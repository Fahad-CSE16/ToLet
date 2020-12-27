from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .models import VehicleServe
from .forms import VehicleForm
from django.views.generic import ListView,DetailView,UpdateView
# Create your views here.
def servicecreate(request):
    if request.method=="POST":
        form=VehicleForm(request.POST)
        if form.is_valid():
            flat=form.save(commit=False)
            flat.user=request.user
            flat.save()
            return redirect('home')
    else:
        form=VehicleForm()
    return render(request,'services/servicecreate.html',{'form':form})

class ServiceList(ListView):
    model=VehicleServe
    queryset=VehicleServe.objects.all()
    template_name='services/servicelist.html'
    context_object_name = 'services'
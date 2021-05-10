from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .models import VehicleServe
from buildings.models import District
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
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["services"] = VehicleServe.objects.all()
        context["district"] = District.objects.all()

        return context
    
def searchServe( request):
    if request.method=='POST':
        queryset=VehicleServe.objects.all()
        vehicle_type=request.POST['type']
        location=request.POST['district']
        servant=request.POST['servant']
        print(vehicle_type,location,servant)
        queryset=queryset.filter(vehicle_type=vehicle_type).filter(labour__gte=servant)
        print(queryset)

        queryset=queryset.filter(location=location)
        print(queryset)
        return render(request,'services/searchresult.html',{'queryset':queryset})
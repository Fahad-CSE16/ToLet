from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .models import FlatImages,Flat,District
from .forms import FlatForm
from django.views.generic import ListView,DetailView,UpdateView,DeleteView
# Create your views here.
def flatcreate(request):
    if request.method=="POST":
        form=FlatForm(request.POST,request.FILES)
        if form.is_valid():
            flat=form.save(commit=False)
            flat.user=request.user
            flat.save()
            return redirect('home')
    else:
        form=FlatForm()
    return render(request,'buildings/flatcreate.html',{'form':form})

class FlatList(ListView):
    model=Flat
    queryset=Flat.objects.all()
    template_name='buildings/flatlist.html'
    context_object_name = 'flats'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['district'] = District.objects.all()
        return context

class FlatDetail(DetailView):
    model = Flat
    context_object_name='post'
    template_name='buildings/flatdetail.html'
class FlatUpdate(UpdateView):
    model = Flat
    form_class=FlatForm
    template_name='buildings/flatcreate.html'
    def get_success_url(self):
        id=self.object.id
        return reverse_lazy('flatdetail', kwargs={'pk': id})
from django.views import View
from django.db.models import Q
class SearchView(View):
    def post(self, request):
        if request.method=='POST':
            queryset=Flat.objects.filter(is_available=True)
            district=request.POST.get('district',None)
            size_from=request.POST.get('size_from',None)
            size_to=request.POST.get('size_to',None)
            price_from=request.POST.get('price_from',None)
            price_to=request.POST.get('price_to',None)
            lift=request.POST.get('lift',None)
            parking=request.POST.get('parking',None)
            gas=request.POST.get('gas',None)
            keyword=request.POST.get('keyword',None)
            print(queryset)
            if keyword:
                query= (Q(details__icontains=keyword)) | (Q(address__icontains=keyword)) 
                queryset=queryset.filter(query)
            print(queryset)
            if gas==1:
                queryset=queryset.filter(gas=gas)
            if parking==1:
                queryset=queryset.filter(parking=parking)
            print(queryset)
            
            if lift==1:
                queryset=queryset.filter(lift=lift)
            if district:
                queryset=queryset.filter(district=district)

            queryset=queryset.filter(size__gte=size_from).filter(size__lte=size_to).filter(rent__gte=price_from).filter(rent__lte=price_to)

            print(queryset)
            return render(request,'search.html',{'queryset':queryset})
from django.http import HttpResponseRedirect
def addphoto(request,id):
    instance=Flat.objects.get(id=id)
    if request.method == 'POST':
        files = request.FILES.get('photo') #field name in model
        file_instance = FlatImages(photo=files, flat=instance)
        file_instance.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def deletephoto(request, id):
    feedfile= FlatImages.objects.get(id=id)
    feedfile.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

from django.core.exceptions import PermissionDenied

def deletetolet(request, id):
    feed= Flat.objects.get(id=id)
    if request.user == feed.user:
        feed.delete()
    else:
        raise PermissionDenied
    return redirect('home')


from django.contrib import admin
from django.urls import path
from .views import changepassview, contactview,loginview,logoutview,registrationview, updateprofile, userprofile
from django.views.generic import TemplateView
urlpatterns = [
    path('signup/', registrationview, name='signup'),
    path('login/', loginview, name='login'),
    path('logout/', logoutview, name='logout'),
    path('changepass/', changepassview, name='changepass'),
    path('contact/', contactview, name='contact'),
    path('userprofile/', userprofile, name='userprofile'),
    path('about/', TemplateView.as_view(template_name='accounts/about_us.html'), name='about'),
    path('updateprofile/',updateprofile, name='updateprofile'),
    

] 

from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('create/',flatcreate, name='flatcreate'),
    path('search/',SearchView.as_view(), name='search'),
    path('<int:pk>/',FlatDetail.as_view(), name='flatdetail'),
    path('delete/<int:id>/',deletetolet, name='deleteflat'),
    path('addphoto/<int:id>/',addphoto, name='addphoto'),
    path('deletephoto/<int:id>/',deletephoto, name='deletephoto'),
    path('update/<int:pk>/',FlatUpdate.as_view(), name='flatupdate'),
] 

from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('create/',servicecreate, name='servicecreate'),
    path('list/',ServiceList.as_view(), name='servicelist'),
    ] 

from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('create/',servicecreate, name='servicecreate'),
    path('searchServe/',searchServe, name='searchServe'),
    path('list/',ServiceList.as_view(), name='servicelist'),
    ] 
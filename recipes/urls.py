from cgitb import html
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

from recipes.views import home



urlpatterns = [
    path('', home),
    
    
    
    
    

] 
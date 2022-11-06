
from django.urls import path
from .views import *

urlpatterns = [
    
    path('', index), 
    path('about/' , about), 
    path('about2/' , about2), 
]

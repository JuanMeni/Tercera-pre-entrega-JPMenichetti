from django.urls import path
from AppProyecto.views import *

urlpatterns = [
    path ('', index, name = 'index'),
    path ('categoria/', categoria, name='categoria'),
    path ('cliente/', cliente, name='cliente'),
    path ('producto/',producto, name='producto'),
]
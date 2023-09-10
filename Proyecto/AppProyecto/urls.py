from django.urls import path
from AppProyecto.views import *

urlpatterns = [
    path ('', index, name = 'index'),
    path ('categorias/', categoria, name='categoria'),
    path ('cliente/', cliente, name='cliente'),
    path ('producto/',producto, name='producto'),
]
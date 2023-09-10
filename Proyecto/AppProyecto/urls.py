from django.urls import path
from AppProyecto.views import *

urlpatterns = [
    path ('categorias/', categoria, name='categoria'),
    path ('cliente/', cliente, name='cliente'),
    path ('producto/',producto, name='producto'),
]
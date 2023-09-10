from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import *

# Create your views here.

def index(req):
    return render (req, "index.html")

def cliente(req):
    return render (req, "cliente.html")

def producto(req):
    return render (req, "producto.html")

def categoria(req):
    return render (req, "categoria.html")
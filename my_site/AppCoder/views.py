import email
from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, Template
from AppCoder.models import *

# Create your views here.

def index(request):
    
    nombre="juan"
    apellido="pesaresi"
    fecha="2001"
    email="juanpablopesaresi@gmail.com"
    
    familia= Familiares(nombre=nombre,apellido=apellido,fechaDeNacimiento=fecha,email=email)
    
    familia.save()
    
    personas=Familiares.objects.all()
    
    ctx={"familia":personas}
    
    return render(request,"index2.html",ctx)
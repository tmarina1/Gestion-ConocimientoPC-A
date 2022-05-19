from turtle import Terminator
from django.contrib import messages
from django.shortcuts import render
from basedatos.models import Archivo 
from basedatos import models
from .models import Archivo
import datetime

# Create your views here.

def index(request):
  searchTerm = request.GET.get('NombreBusqueda')
  if searchTerm:
    mensajes = Archivo.objects.filter(nombre__icontains = searchTerm)
  else:
    mensajes = 'Buscar'

  if request.method == 'POST':
    update = request.POST['update']
    area = request.POST['Area']
    nombre = request.POST['Nombre']
    archivo = request.FILES['Archivo']

    if update != 'Actualizar':
      agregar = models.Archivo(area=area, nombre=nombre, fecha=None, archivo= archivo)
      agregar.save()
      return render(request,'salto.html')
    else:
      actualizarArchivo(area, nombre, archivo)
      return render(request,'salto.html')
  return render(request,'index.html',{'searchTerm':searchTerm,'mensajes':mensajes}) 

def Salto(request):
  return render(request, 'salto.html')

def actualizarArchivo(area, nombre, archivo):
  target = models.Archivo.objects.get(nombre=nombre)
  target.area = area
  target.nombre = nombre
  target.archivo = archivo
  target.save(update_fields=['area', 'nombre', 'archivo'])

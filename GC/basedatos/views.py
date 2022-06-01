from turtle import Terminator
from django.contrib import messages
from django.shortcuts import render
from basedatos.models import Archivo 
from basedatos import models
from .models import Archivo
import datetime
from datetime import datetime

# Create your views here.

def index(request):
  searchTerm = request.GET.get('NombreBusqueda')
  if searchTerm:
    mensajes = Archivo.objects.filter(nombre__icontains = searchTerm)
    try:
      cont = int(mensajes.get().accesos)+1
      mensajes.update(accesos=cont)
    except:
      messages.info(request,'Archivo no encontrado, por favor guárdelo primero.') 
      return render(request,'salto.html')
    #print(dato)
    print(searchTerm)
    print(mensajes)
  else:
    mensajes = 'Buscar'
    #messages.info(request,'Archivo no encontrado, por favor guardelo primero.') 

  if request.method == 'POST':
    update = request.POST['update']
    area = request.POST['Area']
    nombre = request.POST['Nombre']
    fecha = datetime.now()
    archivo = request.FILES['Archivo']

    if verificarPrevioRegistro(nombre) and update != 'Actualizar':
      messages.info(request,'Existe un archivo con este nombre, por favor intenta con otro.') 
      return render(request,'salto.html')

    elif update != 'Actualizar':
      agregar = models.Archivo(area=area, nombre=nombre, fecha=None, archivo= archivo, accesos = 0)
      agregar.save()
      messages.info(request,'¡Guardado exitosamente!') 
      return render(request,'salto.html')
    else:
      try:
        actualizarArchivo(area, nombre, fecha, archivo)
        messages.info(request,'¡Actualizado exitosamente!') 
        return render(request,'salto.html')
      except:
        messages.info(request,'¡No existe el registro que desea actualizar!') 
        return render(request,'salto.html')

  return render(request,'index.html',{'searchTerm':searchTerm,'mensajes':mensajes}) 

def Salto(request):
  return render(request, 'salto.html')

def actualizarArchivo(area, nombre, fecha, archivo):
  target = models.Archivo.objects.get(nombre=nombre)
  target.area = area
  target.nombre = nombre
  target.fecha = fecha
  target.archivo = archivo
  target.save(update_fields=['area', 'nombre', 'fecha', 'archivo'])

def verificarPrevioRegistro(criterio, tipo='nombre'):
    query = False
    
    if tipo == 'nombre':
        query = models.Archivo.objects.filter(nombre=criterio).exists()
    return query

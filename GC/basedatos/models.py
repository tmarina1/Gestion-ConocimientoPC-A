from django.db import models
from pytz import timezone

# Create your models here.

class Archivo(models.Model):
  area = models.CharField(max_length=20, null=False)
  nombre = models.CharField(max_length=20, null=False)
  fecha = models.DateTimeField(auto_now_add=True)
  archivo = models.FileField(upload_to = 'archivos/', null=False)
  accesos = models.SmallIntegerField(null=False)

from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Blog(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=100)
    cuerpo = models.CharField(max_length=1000)
    autor = models.CharField(max_length=80)
    fecha = models.DateField(max_length=80)
    imagen = models.ImageField(upload_to='images', null = True, blank = True)

class Estudiante(models.Model):
    nombre = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField()

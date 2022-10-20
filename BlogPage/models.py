from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=100)
    cuerpo = models.CharField(max_length=1000)
    autor = models.CharField(max_length=80)
    #fecha = models.DateField()
    
    def __str__(self):
        return f"Título:{self.titulo}\Subtitulo:{self.subtitulo}\Autor: {self.autor}"


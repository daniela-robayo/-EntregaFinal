from django.shortcuts import render
from django.http import HttpResponse
from Accounts.forms import form_estudiantes
from Accounts.models import *

# Create your views here.

def create_estudiantes(request):
    if request.method == "POST":
        estudiante = Estudiante(nombre = request.POST['nombre'],password = request.POST['password'],email=request.POST['email'])
        estudiante.save()
        estudiantes = Estudiante.objects.all()
        return render (request,"estudiantesCRUD/read_estudiantes.html",{"estudiantes":estudiantes})
    return render(request,"estudiantesCRUD/create_estudiantes.html")

def read_estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render (request,"estudiantesCRUD/read_estudiantes.html",{"estudiantes":estudiantes})

def update_estudiantes(request, estudiante_email):
    estudiante = Estudiante.objects.get(email = estudiante_email)
    if request.method == 'POST':
        formulario = form_estudiantes(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            estudiante.nombre = informacion['nombre']
            estudiante.password = informacion['password']
            estudiante.email = informacion['email']
            estudiante.save()
            estudiantes = Estudiante.objects.all()
            return render (request,"estudiantesCRUD/read_estudiantes.html",{"estudiantes":estudiantes})
    else:
        formulario = form_estudiantes(initial = {'nombre': estudiante.nombre,'password': estudiante.password,'email': estudiante.email})
    return render(request,"estudiantesCRUD/update_estudiantes.html",{'formulario':formulario})

def delete_estudiantes(request,estudiante_email):
    estudiante = Estudiante.objects.get(email = estudiante_email)
    estudiante.delete()
    estudiantes = Estudiante.objects.all()
    return render (request,"estudiantesCRUD/read_estudiantes.html",{"estudiantes":estudiantes})


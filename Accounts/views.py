from django.shortcuts import render,redirect
from django.http import HttpResponse
from Accounts.forms import form_estudiantes, UserRegisterForm
from Accounts.models import *
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.

def create_estudiantes(request):
    if request.method == "POST":
        estudiante = Estudiante(nombre = request.POST['nombre'],curso = request.POST['curso'],email=request.POST['email'])
        estudiante.save()
        estudiantes = Estudiante.objects.all()
        return render (request,"estudiantesCRUD/read_estudiantes.html",{"estudiantes":estudiantes})
    return render(request,"estudiantesCRUD/create_estudiantes.html")

def read_estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render (request,"estudiantesCRUD/read_estudiantes.html",{"estudiantes":estudiantes})

@login_required
def update_estudiantes(request, estudiante_email):
    estudiante = Estudiante.objects.get(email = estudiante_email)
    if request.method == 'POST':
        formulario = form_estudiantes(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            estudiante.nombre = informacion['nombre']
            estudiante.curso = informacion['curso']
            estudiante.email = informacion['email']
            estudiante.save()
            estudiantes = Estudiante.objects.all()
            return render (request,"estudiantesCRUD/read_estudiantes.html",{"estudiantes":estudiantes})
    else:
        formulario = form_estudiantes(initial = {'nombre': estudiante.nombre,'curso': estudiante.curso,'email': estudiante.email})
    return render(request,"estudiantesCRUD/update_estudiantes.html",{'formulario':formulario})

@login_required
def delete_estudiantes(request,estudiante_email):
    estudiante = Estudiante.objects.get(email = estudiante_email)
    estudiante.delete()
    estudiantes = Estudiante.objects.all()
    return render (request,"estudiantesCRUD/read_estudiantes.html",{"estudiantes":estudiantes})

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            user = form.cleaned_data.get("username")
            pwd = form.cleaned_data.get("password")

            user = authenticate(username = user, password = pwd)
            if user is not None:
                login(request, user)
                return render(request,"home.html")
            else:
                return render(request, "login.html", {'form':form})
        else:
            return render(request, "login.html", {'form':form})
    form = AuthenticationForm()
    return render(request,"login.html",{'form':form})

def signup(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            #username = form.cleaned_data["username"]
            form.save()
            return redirect("/Accounts/login")
        else: 
            return render(request, "registro.html", {'form': form})
    form = UserRegisterForm()
    return render(request, "registro.html", {'form': form})

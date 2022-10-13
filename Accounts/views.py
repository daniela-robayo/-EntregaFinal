from django.shortcuts import render,redirect
from django.http import HttpResponse
from Accounts.forms import form_estudiantes, UserRegisterForm, UserEditForm,ChangePasswordForm
from Accounts.models import *
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm, PasswordChangeForm
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
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

@login_required
def editarPerfil(request):
    usuario = request.user
    user_basic_info = User.objects.get(id = usuario.id)
    form = UserEditForm(request.POST, instance = usuario)
    if request.method == 'POST':
        if form.is_valid():
            user_basic_info.username = form.cleaned_data.get('username')
            user_basic_info.email = form.cleaned_data.get('email')
            user_basic_info.first_name = form.cleaned_data.get('first_name')
            user_basic_info.last_name = form.cleaned_data.get('last_name')
            user_basic_info.save()
            return render(request,"home.html")
        else:
            return render(request,"home.html",{'form':form})
    else: 
        form = UserEditForm(initial = {'email':usuario.email, 'username':usuario.username,'first_name':usuario.first_name, 'last_name':usuario.last_name})
    return render(request, "editarPerfil.html", {'form': form, 'usuario': usuario})

@login_required
def changepass(request):
    usuario = request.user
    if request.method == "POST":
        #form = PasswordChangeForm(data = request.POST, user = usuario)
        form = ChangePasswordForm(data = request.POST, user = request.user)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request,user)
            return render(request, 'home.html')
    else:
        #form = PasswordChangeForm(request.user)
        form = ChangePasswordForm(user = request.user)
    return render(request,'changePass.html',{'form':form,'usuario':usuario})

@login_required
def perfilView(request):
    return render(request,'perfil.html')
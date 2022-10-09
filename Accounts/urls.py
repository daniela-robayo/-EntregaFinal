from turtle import home
from django.urls import path 
from Accounts.views import *
from BlogPage.views import *

urlpatterns = [
    path('', home),
    path('create_estudiantes/',create_estudiantes),
    path('read_estudiantes/',read_estudiantes),
    path('update_estudiantes/<estudiante_email>',update_estudiantes),
    path('delete_estudiantes/<estudiante_email>',delete_estudiantes),
]
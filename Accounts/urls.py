from turtle import home
from django.urls import path 
from Accounts.views import *
from BlogPage.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', home),
    path('signup/',signup),
    path('read_estudiantes/',read_estudiantes),
    path('update_estudiantes/<estudiante_email>',update_estudiantes),
    path('delete_estudiantes/<estudiante_email>',delete_estudiantes),
    path('login/',login_request),
    path('logout/', LogoutView.as_view(template_name = 'logout.html'), name="Logout" ),
    path('create_estudiantes/',create_estudiantes),
]
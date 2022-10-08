from turtle import home
from django.urls import path 
from Accounts.views import *

urlpatterns = [
    path('', home),
]
from django.urls import path, include
from BlogPage.views import *

urlpatterns = [
    path('', home),
    path('home/', home),
    path('AboutUs/', AboutUs),
]
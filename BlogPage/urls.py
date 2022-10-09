from django.urls import path, include
from BlogPage.views import *

urlpatterns = [
    path('', home),
    path('home/', home),
    path('AboutUs/', AboutUs),
    path('formBlog/', formBlog),
    path('pages/', pages),
    path('display_blog/<blog_titulo>', display_blog),
]
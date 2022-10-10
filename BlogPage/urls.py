from django.urls import path, include
from BlogPage.views import *

urlpatterns = [
    path('', home),
    path('home/', home),
    path('AboutUs/', AboutUs),
    path('formBlog/', formBlog),
    path('pages/', pages),
    path('display_blog/<blog_titulo>', display_blog),
    path('delete_blog/<blog_titulo>',delete_blog),
    path('update_blog/<blog_titulo>',update_blog),
]
from django.shortcuts import render
from django.http import HttpResponse
from BlogPage.forms import *
from BlogPage.models import *
# Create your views here.

def home(request):
    return render(request, 'home.html')

def AboutUs(request):
    return render(request, 'aboutUs.html')

def formBlog(request):
    if request.method=="POST":
        blog = Blog(titulo = request.POST['titulo'],subtitulo = request.POST['subtitulo'],autor = request.POST['autor'],fecha = request.POST['fecha'],cuerpo = request.POST['cuerpo'])
        blog.save()
        blogs = Blog.objects.all()
        return render (request,"pages.html",{"blogs":blogs})
    return render(request, 'formBlog.html')

def pages(request):
    blogs = Blog.objects.all()
    return render (request,"pages.html",{"blogs":blogs})


def display_blog(request, blog_titulo):
    blog = Blog.objects.get(titulo = blog_titulo)
    if Blog.objects.filter(titulo__icontains = blog_titulo).values():
            blogs=Blog.objects.filter(titulo__icontains = blog_titulo)
            return render (request,"display_blog.html",{"blogs":blogs})
    else:
        blogs = Blog.objects.all()
        return render (request,"pages.html",{"blogs":blogs})
    #else: 
        #blogs = Blog.objects.all()
        #sreturn render (request,"pages.html",{"blogs":blogs})


    #blog = Blog.objects.get(titulo = blog_titulo)
    #if request.method == 'POST':
        #formulario = form_blogs(request.POST)
        #if formulario.is_valid():
            #blogs = Blog.objects.all()
            #return render (request,"display_blog.html",{"blogs":blogs})
    #else:
        #blogs = Blog.objects.all()
        #return render (request,"pages.html",{"blogs":blogs})


from django.shortcuts import render
from django.http import HttpResponse
from BlogPage.forms import *
from BlogPage.models import *
from django.contrib.auth.decorators import login_required
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

@login_required
def delete_blog(request,blog_titulo):
    blog = Blog.objects.get(titulo = blog_titulo)
    blog.delete()
    blogs = Blog.objects.all()
    return render (request,"pages.html",{"blogs":blogs})

@login_required
def update_blog(request, blog_titulo):
    blog = Blog.objects.get(titulo = blog_titulo)
    if request.method == 'POST':
        formulario = form_blogs(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            blog.titulo = informacion['titulo']
            blog.subtitulo = informacion['subtitulo']
            blog.autor = informacion['autor']
            blog.fecha = informacion['fecha']
            blog.cuerpo = informacion['cuerpo']
            blog.save()
            blogs = Blog.objects.all()
            return render (request,"pages.html",{"blogs":blogs})
    else:
        formulario = form_blogs(initial = {'titulo': blog.titulo,'subtitulo': blog.subtitulo,'autor': blog.autor,'fecha': blog.fecha,'cuerpo': blog.cuerpo})
    return render(request,"update_blog.html",{'formulario':formulario})


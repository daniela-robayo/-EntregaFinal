from django.shortcuts import render
from django.http import HttpResponse
from BlogPage.models import Blog
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
    return render (request,"display_blog.html",{"blog_titulo":blog_titulo})
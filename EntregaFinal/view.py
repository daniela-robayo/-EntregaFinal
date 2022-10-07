from django.http import HttpResponse
from django.template import loader

def home(request):
        planilla = loader.get_template('home.html')
        documento = planilla.render()
        return HttpResponse(documento)
from django import forms

class form_blogs(forms.Form):
    titulo = forms.CharField(max_length=100)
    subtitulo = forms.CharField(max_length=100)
    cuerpo = forms.CharField(max_length=1000)
    autor = forms.CharField(max_length=80)
    fecha = forms.DateField()
    imagen = forms.ImageField()

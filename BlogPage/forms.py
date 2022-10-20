from django import forms

from BlogPage.models import Blog

class form_blogs(forms.Form):
    titulo = forms.CharField(max_length=100)
    subtitulo = forms.CharField(max_length=100)
    cuerpo = forms.CharField(max_length=1000)
    autor = forms.CharField(max_length=80)
    #fecha = forms.DateField()

    class Meta:
        model = Blog
        fields =['titulo','subtitulo','cuerpo','autor']
        #fields =['titulo','subtitulo','cuerpo','autor','fecha']
        help_texts = {k: "" for k in fields }

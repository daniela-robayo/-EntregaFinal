from django import forms

class form_estudiantes(forms.Form):
    nombre = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50)
    email = forms.EmailField()
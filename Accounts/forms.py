from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class form_estudiantes(forms.Form):
    nombre = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50)
    email = forms.EmailField()

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label ="Email")
    password1 = forms.CharField(label = "Contraseña", widget = forms.PasswordInput)
    password2 = forms.CharField(label = "Confirmar contraseña", widget = forms.PasswordInput)

    class Meta:
        model = User
        fields =['username','email','password1','password2']
        help_text = {k: "" for k in fields }
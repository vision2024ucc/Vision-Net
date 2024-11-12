from django import forms
from .models import Usuario

class Registrar_usuario(forms.Form):
    primer_nombre = forms.CharField(max_length=200)
    segundo_nombre = forms.CharField(max_length=200)
    nombre_usuario = forms.CharField(max_length=200)
    emial = forms.EmailField()
    contraseña = forms.CharField(widget=forms.PasswordInput)


    
    
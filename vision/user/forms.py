# files.py
from django import forms



class RegistrationForm(forms.Form):
    primer_nombre = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Primer nombre'}))
    segundo_nombre = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Segundo nombre'}))
    apellido = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido'}))
    nombre_usuario = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Nombre de usuario"), error_messages={'invalid': ("El nombre de usuario debe contener solo letras,numeros y guiones bajos")})
    email = forms.EmailField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Email"))
    contraseña_1 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label=_("Contraseña"))
    contraseña_2 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label=_("Repita la contraseña"))

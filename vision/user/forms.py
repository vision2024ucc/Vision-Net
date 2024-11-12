# files.py
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class RegistrationForm(forms.Form):
    primer_nombre = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Primer nombre'}))
    segundo_nombre = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Segundo nombre'}))
    apellido = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido'}))
    nombre_usuario = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Nombre de usuario"), error_messages={'invalid': ("El nombre de usuario debe contener solo letras,numeros y guiones bajos")})
    email = forms.EmailField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Email"))
    contraseña_1 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label=_("Contraseña"))
    contraseña_2 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label=_("Repita la contraseña"))

    def clean_username(self):
        try:
            User.objects.get(nombre_usuario__iexact=self.cleaned_data['nombre_usuario'])
        except User.DoesNotExist:
            return self.cleaned_data['nombre_usurio']
        raise forms.ValidationError(_("El nombre de usuario ya existe. Por favor prueba con otro."))

    def clean_email(self):
        try:
            User.objects.get(email__iexact=self.cleaned_data['email'])
        except User.DoesNotExist:
            return self.cleaned_data['email']
        raise forms.ValidationError(_("El email ya existe. Por favor prueba con otro."))

    def clean(self):
        if 'contrseña_1' in self.cleaned_data and 'contraseña_1' in self.cleaned_data:
            if self.cleaned_data['contraseña_1'] != self.cleaned_data['contraseña_2']:
                raise forms.ValidationError(_("Los dos campos de contraseña no coincidían."))
        return self.cleaned_data
    
    
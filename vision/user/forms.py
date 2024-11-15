from django import forms
from django.core.exceptions import ValidationError
from .models import Usuario,Publicacion

class registro_form(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = [
            "primer_nombre",
            "segundo_nombre",
            "nombre_usuario",
            "email",
            "contraseña",
        ]
        labels = {
            'primer_nombre': 'Primer Nombre',
            'segundo_nombre': 'Segundo Nombre',
            'nombre_usuario': 'Nombre Usuario',
            'email': 'Email',
            'contraseña': 'Contraseña',
        }
        widgets = {
            'primer_nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Primer Nombre'}),
            'segundo_nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Segundo Nombre'}),
            'nombre_usuario': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de usuario'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'contraseña': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña', 'required': True, 'max_length': 30, 'render_value': False}),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Usuario.objects.filter(email=email).exists():
            raise ValidationError("Este correo electrónico ya está registrado.")
        return email

    def clean_contraseña(self):
        contraseña = self.cleaned_data.get('contraseña')
        # Validación de contraseña (ejemplo: al menos 8 caracteres y 1 número)
        if len(contraseña) < 8 or not any(char.isdigit() for char in contraseña):
            raise ValidationError("La contraseña debe tener al menos 8 caracteres y contener al menos un número.")
        return contraseña

    def clean(self):
        cleaned_data = super().clean()
        primer_nombre = cleaned_data.get('primer_nombre')
        segundo_nombre = cleaned_data.get('segundo_nombre')

        # Ejemplo de validación: ambos nombres no pueden ser iguales
        if primer_nombre and segundo_nombre and primer_nombre == segundo_nombre:
            raise ValidationError("El primer y segundo nombre no pueden ser iguales.")
        
        
        return cleaned_data
    
class iniciar_form(forms.ModelForm):

    class Meta:
        model = Usuario
        
        fields =[
            "nombre_usuario",
            "contraseña",
        ]
        
        labels ={
            'nombre_usuario': 'Nombre Usuario',
            'contraseña': 'Contraseña',
        }

        widgets  ={
            'nombre_usuario': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de usuario'}),
            'contraseña': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña', 'required': True, 'max_length': 30, 'render_value': False}),
        }

class publicacion_form(forms.ModelForm):
    class Meta:
        model = Publicacion
        fields = [
            "titulo",
            "descripcion",
            "archivo",
        ]
        labels = {
            'titulo': 'Título de la publicación',
            'descripcion': 'Descripción de la publicación',
            'archivo': 'Sube cualquier tipo de archivo (opcional)',
        }
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'archivo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

from django.shortcuts import render,HttpResponseRedirect,get_object_or_404
from .forms import registro_form
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import iniciar_form

def Incio (request):
    return render(request,'base.html')

from django.shortcuts import render, redirect
from .forms import registro_form, iniciar_form

def Registro(request):
    if request.method == 'POST':
        form = registro_form(request.POST)
        if form.is_valid():
            # Aquí puedes procesar los datos válidos
            form.save()  # Por ejemplo, guardar el usuario
            return redirect('base.html')  # Redirige a la página deseada
    else:
        form = registro_form()
    
    return render(request, 'registrar_usuario.html', {'form': form})

def iniciar_seccion(request):
    if request.method == 'POST':
        form = iniciar_form(request.POST)
        
        if form.is_valid():
            nombre_usuario = form.cleaned_data.get('nombre_usuario')
            contraseña = form.cleaned_data.get('contraseña')
            
            # Autenticamos al usuario
            usuario = authenticate(request, username=nombre_usuario, password=contraseña)
            
            if usuario is not None:
                # Inicia la sesión del usuario
                login(request, usuario)
                return redirect('base.html')  # Redirige a la página de inicio u otra página deseada
            else:
                # Si la autenticación falla, muestra un mensaje de error
                messages.error(request, 'Nombre de usuario o contraseña incorrectos')
        else:
            # Si el formulario no es válido, muestra un mensaje de error genérico
            messages.error(request, 'Por favor corrige los errores en el formulario')
    else:
        form = iniciar_form()
    
    return render(request, 'iniciar.html', {'form': form})

        




    



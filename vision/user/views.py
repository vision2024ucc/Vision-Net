from django.shortcuts import render,HttpResponseRedirect,get_object_or_404
from .forms import registro_form

def Incio (request):
    return render(request,'base.html')

from django.shortcuts import render, redirect
from .forms import registro_form

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




    



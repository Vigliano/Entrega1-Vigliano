from django.shortcuts import render
from .models import *
from Miapp.forms import *
from django.http import HttpResponse


# Create your views here.

def index_html(request):
    return render(request, 'Miapp/index.html')



#------------------------------Auto----------------------------------

def auto_html(request):
    return render(request, 'Miapp/auto.html')

def insertar_auto(request):
    if request.method == 'POST':
        formulario= AutoFormulario(request.POST)
        print(formulario)
        if formulario.is_valid:
            informacion = formulario.cleaned_data
            auto = Auto(marca=informacion['marca'], modelo=informacion['modelo'], fabricacion=informacion['fabricacion'], kilometraje=informacion['kilometraje'])
            auto.save()
            return render(request, 'Miapp/index.html')

    else:
        formulario = AutoFormulario()

    return render(request, 'Miapp/insertar_auto.html', {'formulario':formulario})

def buscar_auto(request):
    if request.GET.get('marca', False):
        marca = request.GET['marca']
        autos = Auto.objects.filter(marca__icontains=marca)
        print(autos)
        return render(request, 'Miapp/buscar_auto.html', {'autos':autos})
        
 
    else:
        respuesta = 'Ese vehiculo no esta registrado'

        return render(request, 'Miapp/buscar_auto.html', {'respuesta':respuesta})


# -----------------------------Camioneta-----------------------------------  

def camioneta_html(request):
    return render(request, 'Miapp/camioneta.html')

def insertar_camioneta(request):
    if request.method == 'POST':
        formulario= CamionetaFormulario(request.POST)
        print(formulario)
        if formulario.is_valid:
            informacion = formulario.cleaned_data
            auto = Camioneta(marca=informacion['marca'], modelo=informacion['modelo'], fabricacion=informacion['fabricacion'], kilometraje=informacion['kilometraje'])
            auto.save()
            return render(request, 'Miapp/index.html')

    else:
        formulario = AutoFormulario()

    return render(request, 'Miapp/insertar_auto.html', {'formulario':formulario})

def buscar_camioneta(request):
    if request.GET.get('marca', False):
        marca = request.GET['marca']
        camionetas = Camioneta.objects.filter(marca__icontains=marca)
        print(camionetas)
        return render(request, 'Miapp/buscar_camioneta.html', {'camionetas':camionetas})
        
 
    else:
        respuesta = 'Ese vehiculo no esta registrado'

        return render(request, 'Miapp/buscar_camioneta.html', {'respuesta':respuesta})



#-----------------------------Moto-----------------------------------

def moto_html(request):
    return render(request, 'Miapp/moto.html')

def insertar_moto(request):
    if request.method == 'POST':
        formulario= MotoFormulario(request.POST)
        print(formulario)
        if formulario.is_valid:
            informacion = formulario.cleaned_data
            auto = Moto(marca=informacion['marca'], modelo=informacion['modelo'], fabricacion=informacion['fabricacion'], kilometraje=informacion['kilometraje'])
            auto.save()
            return render(request, 'Miapp/index.html')

    else:
        formulario = MotoFormulario()

    return render(request, 'Miapp/insertar_moto.html', {'formulario':formulario})

def buscar_moto(request):
    if request.GET.get('marca', False):
        marca = request.GET['marca']
        motos = Moto.objects.filter(marca__icontains=marca)
        print(motos)
        return render(request, 'Miapp/buscar_moto.html', {'motos':motos})
        
 
    else:
        respuesta = 'Ese vehiculo no esta registrado'

        return render(request, 'Miapp/buscar_auto.html', {'respuesta':respuesta})




    




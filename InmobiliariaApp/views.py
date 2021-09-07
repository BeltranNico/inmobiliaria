from django.shortcuts import render, HttpResponse
from inmuebles.models import Inmueble, Operacion, Imagenes



# Create your views here.

def home(request):

    # inmuebles=Inmueble.objects.all()
    ventas=Inmueble.objects.filter(operacion=1)
    alquileres=Inmueble.objects.filter(operacion=2)
  
    return render(request, "InmobiliariaApp/home.html", {"ventas" : ventas, "alquileres": alquileres})

def alquiler(request, propiedad_id):

    inmuebles=Inmueble.objects.get(id=propiedad_id)
    imagenes=Imagenes.objects.filter(inmueble_id=propiedad_id)
    
    return render(request, "InmobiliariaApp/alquiler.html", {"inmuebles": inmuebles, "imagenes": imagenes})

def venta(request, propiedad_id):

    inmuebles=Inmueble.objects.get(id=propiedad_id)
    imagenes=Imagenes.objects.filter(inmueble_id=propiedad_id)
    
    return render(request, "InmobiliariaApp/venta.html", {"inmuebles": inmuebles, "imagenes": imagenes})

def propiedad(request, propiedad_id):
    
    inmuebles=Inmueble.objects.get(id=propiedad_id)
    imagenes=Imagenes.objects.filter(inmueble_id=propiedad_id)
    

    return render(request, "InmobiliariaApp/propiedad.html", {"inmuebles": inmuebles, "imagenes": imagenes})
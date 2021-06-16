from django.shortcuts import render, HttpResponse
from inmuebles.models import Inmueble, Operacion



# Create your views here.

def home(request):

    # inmuebles=Inmueble.objects.all()
    ventas=Inmueble.objects.filter(operacion=1)
    alquileres=Inmueble.objects.filter(operacion=2)
  
    return render(request, "InmobiliariaApp/home.html", {"ventas" : ventas, "alquileres": alquileres})

def alquiler(request):

    inmuebles=Inmueble.objects.filter(operacion=2)
    
    return render(request, "InmobiliariaApp/alquiler.html", {"inmuebles" : inmuebles})
    
def venta(request):

    inmuebles=Inmueble.objects.filter(operacion=1)
    
    return render(request, "InmobiliariaApp/venta.html", {"inmuebles" : inmuebles})


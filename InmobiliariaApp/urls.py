from django.urls import path
from InmobiliariaApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="Home"),
    # path('propiedad/<int:propiedad_id>', views.propiedad, name="Propiedad"),
    path('alquiler/<int:propiedad_id>', views.alquiler, name="Alquiler"),
    path('venta/<int:propiedad_id>', views.venta, name="Venta"),
    

]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
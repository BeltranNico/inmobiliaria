from django.urls import path
from InmobiliariaApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="Home"),
    path('alquiler', views.alquiler, name="Alquiler"),
    path('venta', views.venta, name="Venta"),
    

]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
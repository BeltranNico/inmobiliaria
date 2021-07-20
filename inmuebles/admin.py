from django.contrib import admin
from .models import Categoria, Ambiente, Operacion, Ciudad, Inmueble, Imagenes

# Register your models here.

class CategoriasAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')

class AmbienteAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')

class OperacionAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')

class CiudadAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')

class InmuebleAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')

class ImagenesAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')

admin.site.register(Categoria, CategoriasAdmin)
admin.site.register(Ambiente, AmbienteAdmin)
admin.site.register(Operacion, OperacionAdmin)
admin.site.register(Ciudad, CiudadAdmin)
admin.site.register(Inmueble, InmuebleAdmin)
admin.site.register(Imagenes, ImagenesAdmin)
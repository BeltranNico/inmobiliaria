#from _typeshed import Self
from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='categoria'
        verbose_name_plural='categorias'

    def __str__(self):
        return self.nombre

class Ambiente(models.Model):
    nombre=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='ambiente'
        verbose_name_plural='ambientes'

    def __str__(self):
        return self.nombre

class Operacion(models.Model):
    nombre=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='operacion'
        verbose_name_plural='operaciones'

    def __str__(self):
        return self.nombre

class Ciudad(models.Model):
    nombre=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='ciudad'
        verbose_name_plural='ciudades'

    def __str__(self):
        return self.nombre



class Inmueble(models.Model):
    direccion=models.CharField(max_length=50)
    titulo=models.CharField(max_length=140, null=True, blank=True)
    ciudad=models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE)
    ambiente=models.ForeignKey(Ambiente, on_delete=models.CASCADE)
    metros=models.FloatField(null=True, blank=True)
    antiguedad=models.IntegerField(null=True, blank=True)
    operacion=models.ManyToManyField(Operacion)
    precio=models.CharField(max_length=20, default="Consultar")
    caracteristicas=models.TextField(null=True, blank=True)
    requisitos=models.TextField(null=True, blank=True)
    imagen=models.ImageField(upload_to='inmueble')
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    
    
    class Meta: 
        verbose_name='inmueble'
        verbose_name_plural='inmuebles'

    def __str__(self):
        return self.direccion

class Imagenes(models.Model):
    inmueble=models.ForeignKey(Inmueble, on_delete=models.CASCADE)
    direccion=models.CharField(max_length=50, default="Referencia")
    imagen=models.ImageField(upload_to='inmueble')
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta: 
        verbose_name='imagen'
        verbose_name_plural='imagenes'

    def __str__(self):
        return self.direccion
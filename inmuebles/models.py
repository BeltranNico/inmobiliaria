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
    imagen1=models.ImageField(upload_to='inmueble', null=True, blank=True)
    imagen2=models.ImageField(upload_to='inmueble', null=True, blank=True)
    imagen3=models.ImageField(upload_to='inmueble', null=True, blank=True)
    imagen4=models.ImageField(upload_to='inmueble', null=True, blank=True)
    imagen5=models.ImageField(upload_to='inmueble', null=True, blank=True)
    imagen6=models.ImageField(upload_to='inmueble', null=True, blank=True)
    imagen7=models.ImageField(upload_to='inmueble', null=True, blank=True)
    imagen8=models.ImageField(upload_to='inmueble', null=True, blank=True)
    imagen9=models.ImageField(upload_to='inmueble', null=True, blank=True)
    destacado=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    
    
    class Meta: 
        verbose_name='inmueble'
        verbose_name_plural='inmuebles'

    def __str__(self):
        return self.direccion

    
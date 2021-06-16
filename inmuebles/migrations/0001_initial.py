# Generated by Django 3.1.5 on 2021-03-02 00:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ambiente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'ambiente',
                'verbose_name_plural': 'ambientes',
            },
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'categoria',
                'verbose_name_plural': 'categorias',
            },
        ),
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'ciudad',
                'verbose_name_plural': 'ciudades',
            },
        ),
        migrations.CreateModel(
            name='Operacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'operacion',
                'verbose_name_plural': 'operaciones',
            },
        ),
        migrations.CreateModel(
            name='Inmueble',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion', models.CharField(max_length=50)),
                ('precio', models.BigIntegerField(blank=True, default='Consultar', null=True)),
                ('caracteristicas', models.TextField(blank=True, null=True)),
                ('requisitos', models.TextField(blank=True, null=True)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='inmueble')),
                ('imagen1', models.ImageField(blank=True, null=True, upload_to='inmueble')),
                ('imagen2', models.ImageField(blank=True, null=True, upload_to='inmueble')),
                ('imagen3', models.ImageField(blank=True, null=True, upload_to='inmueble')),
                ('imagen4', models.ImageField(blank=True, null=True, upload_to='inmueble')),
                ('imagen5', models.ImageField(blank=True, null=True, upload_to='inmueble')),
                ('imagen6', models.ImageField(blank=True, null=True, upload_to='inmueble')),
                ('imagen7', models.ImageField(blank=True, null=True, upload_to='inmueble')),
                ('imagen8', models.ImageField(blank=True, null=True, upload_to='inmueble')),
                ('imagen9', models.ImageField(blank=True, null=True, upload_to='inmueble')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('ambiente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inmuebles.ambiente')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inmuebles.categoria')),
                ('ciudad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inmuebles.ciudad')),
                ('operacion', models.ManyToManyField(to='inmuebles.Operacion')),
            ],
            options={
                'verbose_name': 'inmueble',
                'verbose_name_plural': 'inmuebles',
            },
        ),
    ]

# Generated by Django 3.2.4 on 2021-07-19 20:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inmuebles', '0013_inmueble_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagenes',
            name='direccion',
            field=models.CharField(default=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inmuebles.inmueble'), max_length=50),
        ),
    ]

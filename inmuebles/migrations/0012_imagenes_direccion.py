# Generated by Django 3.2.4 on 2021-07-19 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inmuebles', '0011_alter_imagenes_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagenes',
            name='direccion',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
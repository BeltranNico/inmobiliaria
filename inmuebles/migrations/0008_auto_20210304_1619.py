# Generated by Django 3.1.5 on 2021-03-04 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inmuebles', '0007_auto_20210303_0106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inmueble',
            name='destacado',
            field=models.BooleanField(default=False),
        ),
    ]

# Generated by Django 3.1.5 on 2021-03-03 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inmuebles', '0003_auto_20210302_1531'),
    ]

    operations = [
        migrations.AddField(
            model_name='inmueble',
            name='destacado',
            field=models.BooleanField(default=True),
        ),
    ]
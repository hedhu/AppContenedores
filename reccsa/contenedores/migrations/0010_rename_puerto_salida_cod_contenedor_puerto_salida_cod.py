# Generated by Django 4.2.7 on 2023-11-25 16:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenedores', '0009_contenedor_estado'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contenedor',
            old_name='puerto_Salida_cod',
            new_name='puerto_salida_cod',
        ),
    ]
# Generated by Django 3.0.5 on 2022-06-18 16:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0030_auto_20220617_2255'),
    ]

    operations = [
        migrations.RenameField(
            model_name='administrador',
            old_name='administrador_codigo',
            new_name='codigo',
        ),
        migrations.RenameField(
            model_name='paciente',
            old_name='paciente_codigo',
            new_name='codigo',
        ),
        migrations.RenameField(
            model_name='vacunador',
            old_name='vacunador_codigo',
            new_name='codigo',
        ),
    ]

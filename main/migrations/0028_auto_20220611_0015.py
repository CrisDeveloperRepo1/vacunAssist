# Generated by Django 3.0.5 on 2022-06-11 03:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0027_auto_20220611_0005'),
    ]

    operations = [
        migrations.RenameField(
            model_name='administrador',
            old_name='administrador_contraseña',
            new_name='contraseña',
        ),
    ]

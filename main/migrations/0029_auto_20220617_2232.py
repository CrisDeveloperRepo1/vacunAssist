# Generated by Django 3.0.5 on 2022-06-18 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0028_auto_20220611_0015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='administrador',
            name='administrador_codigo',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='contraseña',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='vacunador',
            name='contraseña',
            field=models.CharField(max_length=200),
        ),
    ]
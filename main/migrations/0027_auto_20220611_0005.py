# Generated by Django 3.0.5 on 2022-06-11 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0026_auto_20220609_1118'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='contraseña',
            field=models.IntegerField(default=int),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vacunador',
            name='contraseña',
            field=models.IntegerField(default=int),
            preserve_default=False,
        ),
    ]

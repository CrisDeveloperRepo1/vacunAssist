# Generated by Django 3.0.5 on 2022-06-09 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_solicitudturnofa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='paciente_codigo',
            field=models.PositiveIntegerField(default=0),
        ),
    ]

# Generated by Django 4.1.dev20220516154624 on 2022-07-06 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0038_paciente_st_vac_gripe_asistencia'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='vac_Gripe_asistencia',
            field=models.SmallIntegerField(choices=[(1, 'Si'), (2, 'No')], default=2),
        ),
    ]

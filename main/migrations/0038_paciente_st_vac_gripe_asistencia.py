# Generated by Django 4.1.dev20220516154624 on 2022-07-05 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0037_paciente_st_vac_amarilla_aplicada_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente_st',
            name='vac_Gripe_asistencia',
            field=models.SmallIntegerField(choices=[(1, 'Si'), (2, 'No')], default=2),
        ),
    ]

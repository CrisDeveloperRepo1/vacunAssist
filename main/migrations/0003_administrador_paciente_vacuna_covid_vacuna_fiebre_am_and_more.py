# Generated by Django 4.1.dev20220516154624 on 2022-05-23 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20220516_1912'),
    ]

    operations = [
        migrations.CreateModel(
            name='Administrador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('administrador_nombre', models.CharField(max_length=200)),
                ('administrador_apellido', models.CharField(max_length=20)),
                ('administrador_fechaNac', models.DateTimeField(verbose_name='fecha nacimiento')),
                ('administrador_zona', models.CharField(max_length=200)),
                ('administrador_dni', models.IntegerField()),
                ('administrador_email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paciente_nombre', models.CharField(max_length=200)),
                ('paciente_apellido', models.CharField(max_length=20)),
                ('paciente_fechaNac', models.DateTimeField(verbose_name='fecha nacimiento')),
                ('paciente_zona', models.CharField(max_length=200)),
                ('paciente_dni', models.IntegerField()),
                ('paciente_email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Vacuna_Covid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vac_Covid1_aplicada', models.SmallIntegerField(choices=[(1, 'Si'), (2, 'No')], default=2)),
                ('vac_Covid2_aplicada', models.SmallIntegerField(choices=[(1, 'Si'), (2, 'No')], default=2)),
                ('vac_Covid_turno1', models.DateTimeField(verbose_name='turno_1era')),
                ('vac_Covid_turno2', models.DateTimeField(verbose_name='turno_2da')),
                ('vac_Covid1era_asistencia', models.SmallIntegerField(choices=[(1, 'Si'), (2, 'No')], default=2)),
                ('vac_Covid2da_asistencia', models.SmallIntegerField(choices=[(1, 'Si'), (2, 'No')], default=2)),
                ('stock_vac_covid', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Vacuna_Fiebre_Am',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vac_Amarilla_aplicada', models.SmallIntegerField(choices=[(1, 'Si'), (2, 'No')], default=2)),
                ('vac_Amarilla_turno', models.DateTimeField(verbose_name='turno')),
                ('vac_Amarilla_asistencia', models.SmallIntegerField(choices=[(1, 'Si'), (2, 'No')], default=2)),
                ('stock_vac_fa', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Vacuna_Gripe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vac_Gripe_aplicada', models.SmallIntegerField(choices=[(1, 'Si'), (2, 'No')], default=2)),
                ('vac_Gripe_turno', models.DateTimeField(verbose_name='turno')),
                ('vac_Amarilla_asistencia', models.SmallIntegerField(choices=[(1, 'Si'), (2, 'No')], default=2)),
                ('stock_vac_gripe', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Vacunatorio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('administrador_nombre', models.CharField(max_length=100)),
                ('stock_vac_fa', models.IntegerField()),
                ('stock_vac_covid', models.IntegerField()),
                ('stock_vac_gripe', models.IntegerField()),
            ],
        ),
    ]

# Generated by Django 3.0.5 on 2022-05-27 01:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_administrador_paciente_vacuna_covid_vacuna_fiebre_am_vacuna_gripe_vacunador_vacunatorio'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacunatorio',
            name='vacunatorio_unidad',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vacunatorio',
            name='vacunatorio_zona',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Envio_de_correo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('subject', models.CharField(max_length=250)),
                ('body', models.TextField(blank=True, null=True)),
                ('email', models.ManyToManyField(to='main.Vacunador')),
            ],
        ),
    ]

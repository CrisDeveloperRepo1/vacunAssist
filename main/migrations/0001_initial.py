# Generated by Django 3.0.5 on 2022-05-16 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vacunador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vacunador_fechaNac', models.DateTimeField(verbose_name='fecha nacimiento')),
                ('vacunador_zona', models.CharField(max_length=200)),
                ('vacunador_dni', models.IntegerField()),
                ('vacunador_email', models.EmailField(max_length=254)),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asiento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('no_asiento', models.CharField(max_length=4)),
                ('estado_asiento', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('modelo_bus', models.CharField(max_length=4)),
                ('placa_bus', models.CharField(max_length=15)),
                ('no_asiento_bus', models.CharField(max_length=4)),
                ('imagen_bus', models.ImageField(upload_to='imagen/')),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('nombre_cliente', models.CharField(max_length=50)),
                ('apellido_cliente', models.CharField(max_length=50)),
                ('edad_cliente', models.CharField(max_length=2)),
                ('genero_cliente', models.CharField(max_length=1)),
                ('telefono_cliente', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Destino',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('lugar_destino', models.CharField(max_length=50)),
                ('valor_destino', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Programacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('fecha', models.DateTimeField(verbose_name='fecha salida')),
                ('hora', models.CharField(max_length=10)),
                ('id_bus', models.ForeignKey(to='blog.Bus')),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('fecha_reserva', models.DateTimeField(verbose_name='fecha Reserva')),
                ('cliente', models.ForeignKey(to='blog.Cliente')),
                ('destino', models.ForeignKey(to='blog.Destino')),
                ('programacion', models.ForeignKey(to='blog.Programacion')),
            ],
        ),
        migrations.AddField(
            model_name='cliente',
            name='destinos',
            field=models.ManyToManyField(to='blog.Destino', through='blog.Reserva'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='programaciones',
            field=models.ManyToManyField(to='blog.Programacion', through='blog.Reserva'),
        ),
        migrations.AddField(
            model_name='asiento',
            name='id_bus',
            field=models.ForeignKey(to='blog.Bus'),
        ),
    ]

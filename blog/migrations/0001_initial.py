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
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('no_asiento', models.CharField(max_length=4)),
                ('estado_asiento', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('modelo_bus', models.CharField(max_length=4)),
                ('placa_bus', models.CharField(max_length=15)),
                ('no_asiento_bus', models.CharField(max_length=4)),
                ('imagen_bus', models.ImageField(upload_to='media/Fotos/')),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('NIT_cliente', models.CharField(max_length=10)),
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
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('lugar_destino', models.CharField(max_length=50)),
                ('valor_destino', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Programacion',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
                ('id_bus', models.ForeignKey(to='blog.Bus')),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('fecha_reserva', models.DateField(verbose_name='fecha Reserva')),
                ('cliente', models.ForeignKey(to='blog.Cliente')),
                ('destino', models.ForeignKey(to='blog.Destino')),
                ('programacion', models.ForeignKey(to='blog.Programacion')),
            ],
        ),
        migrations.AddField(
            model_name='cliente',
            name='destinos',
            field=models.ManyToManyField(through='blog.Reserva', to='blog.Destino'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='programaciones',
            field=models.ManyToManyField(through='blog.Reserva', to='blog.Programacion'),
        ),
        migrations.AddField(
            model_name='asiento',
            name='id_bus',
            field=models.ForeignKey(to='blog.Bus'),
        ),
    ]

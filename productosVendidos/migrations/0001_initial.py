# Generated by Django 5.1.1 on 2024-09-17 19:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TicketCabecera',
            fields=[
                ('id_ticketCabecera', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField(verbose_name='Fecha')),
                ('nombreCliente', models.CharField(max_length=100, verbose_name='Cliente')),
                ('celular', models.CharField(max_length=11, verbose_name='Celular')),
                ('distrito', models.CharField(max_length=100, verbose_name='Distrito')),
                ('total', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Total')),
            ],
        ),
        migrations.CreateModel(
            name='TicketDetalle',
            fields=[
                ('id_ticketDetalle', models.AutoField(primary_key=True, serialize=False)),
                ('nombreProducto', models.CharField(max_length=100, verbose_name='Producto')),
                ('precioUnidad', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Precio Unidad')),
                ('cantidad', models.IntegerField(verbose_name='Cantidad')),
                ('id_ticketCabecera', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productosVendidos.ticketcabecera')),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-19 10:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha Creacion')),
                ('customer', models.CharField(blank=True, max_length=100, null=True, verbose_name='Cliente')),
                ('price', models.IntegerField(blank=True, null=True, verbose_name='Precio')),
                ('discount', models.IntegerField(blank=True, null=True, verbose_name='Descuento')),
                ('image_local_path', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Path Local Image')),
                ('name', models.CharField(blank=True, max_length=200, null=True, verbose_name='Name')),
                ('description', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Description')),
                ('category', models.CharField(blank=True, max_length=600, null=True, verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
            },
        ),
    ]

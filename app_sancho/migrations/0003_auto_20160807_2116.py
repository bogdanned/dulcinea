# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-07 21:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_sancho', '0002_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerDatabase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(blank=True, max_length=100, null=True, verbose_name='Lenguaje Web')),
                ('password', models.CharField(blank=True, max_length=100, null=True, verbose_name='Framework Web')),
                ('port', models.CharField(blank=True, max_length=100, null=True, verbose_name='Base de Datos')),
                ('db_type', models.CharField(blank=True, max_length=100, null=True, verbose_name='Base de Datos')),
                ('host', models.CharField(blank=True, max_length=100, null=True, verbose_name='Base de Datos')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Base de Datos')),
            ],
        ),
        migrations.CreateModel(
            name='CustomerStack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('web_language', models.CharField(blank=True, max_length=100, null=True, verbose_name='Lenguaje Web')),
                ('web_framework', models.CharField(blank=True, max_length=100, null=True, verbose_name='Framework Web')),
                ('database_type', models.CharField(blank=True, max_length=100, null=True, verbose_name='Base de Datos')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='customer_product_id',
            field=models.CharField(blank=True, max_length=600, null=True, verbose_name='Customer Product ID'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='nr_products',
            field=models.IntegerField(blank=True, null=True, verbose_name='Nr. Productos'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(blank=True, max_length=600, null=True, verbose_name='Categoria'),
        ),
        migrations.AddField(
            model_name='customerstack',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_sancho.Customer'),
        ),
        migrations.AddField(
            model_name='customerdatabase',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_sancho.Customer'),
        ),
    ]

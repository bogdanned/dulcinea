# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-09 15:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_sancho', '0006_auto_20160809_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='customer_parent_category',
            field=models.CharField(blank=True, max_length=600, null=True, verbose_name='Categoria Padre'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(blank=True, max_length=400, null=True, verbose_name='Name'),
        ),
    ]

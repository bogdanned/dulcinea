# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-20 09:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_sancho', '0002_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='nr_products',
            field=models.IntegerField(blank=True, null=True, verbose_name='Nr. Productos'),
        ),
    ]

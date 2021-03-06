# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-09 11:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_sancho', '0004_auto_20160809_0327'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_category_id', models.CharField(blank=True, max_length=600, null=True, verbose_name='Customer Product ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True, verbose_name='Name')),
                ('description', models.TextField(blank=True, max_length=10000, null=True, verbose_name='Description Larga')),
                ('customer', models.CharField(blank=True, max_length=100, null=True, verbose_name='Cliente')),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(to='app_sancho.Category', verbose_name='Categoria'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-10 22:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_galgo', '0007_auto_20160810_1912'),
    ]

    operations = [
        migrations.CreateModel(
            name='FbAd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad_field_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='AdName')),
                ('ad_field_status', models.CharField(blank=True, max_length=100, null=True, verbose_name='AdCreationStatus')),
            ],
        ),
        migrations.CreateModel(
            name='FbAdCreatives',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adcreative_field_message', models.CharField(blank=True, max_length=100, null=True, verbose_name='AdMessage')),
                ('adcreative_field_link', models.CharField(blank=True, max_length=100, null=True, verbose_name='AdURL')),
                ('adcreative_field_caption', models.CharField(blank=True, max_length=100, null=True, verbose_name='AdText')),
                ('adcreative_field_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='AdCreativeName')),
            ],
        ),
        migrations.CreateModel(
            name='FbAdSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('target_audience_type_term', models.CharField(blank=True, max_length=100, null=True, verbose_name='q')),
                ('target_audience_search_type', models.CharField(blank=True, max_length=100, null=True, verbose_name='type')),
                ('geo_locations_countries', models.CharField(blank=True, max_length=100, null=True, verbose_name='GeoLocationCountry')),
                ('age_min', models.IntegerField(blank=True, null=True, verbose_name='age_min')),
                ('age_max', models.IntegerField(blank=True, null=True, verbose_name='age_max')),
                ('adset_field_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='AdSetName')),
                ('adset_field_daily_budget', models.IntegerField(blank=True, null=True, verbose_name='DailyBudget')),
                ('adset_filed_billing_event', models.CharField(default='AdSet.BillingEvent.impressions', max_length=100, null=True, verbose_name='Billing')),
                ('adset_field_optimization_goal', models.CharField(blank=True, max_length=100, null=True, verbose_name='AdSetOptimizationGoal')),
                ('adset_field_bid_amount', models.IntegerField(blank=True, null=True, verbose_name='IntegerField')),
                ('campaign', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_galgo.FbCampaign')),
            ],
        ),
        migrations.DeleteModel(
            name='FbAdCreationData',
        ),
        migrations.DeleteModel(
            name='FbAdCreativesCreationData',
        ),
        migrations.DeleteModel(
            name='FbAdSetCreationData',
        ),
        migrations.AddField(
            model_name='fbadcreatives',
            name='adset',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_galgo.FbAdSet'),
        ),
        migrations.AddField(
            model_name='fbad',
            name='adcreative',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_galgo.FbAdCreatives'),
        ),
    ]

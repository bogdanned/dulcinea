# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-09 12:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_galgo', '0002_auto_20160809_1208'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerFbAdCreationData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad_field_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='AdName')),
                ('ad_field_status', models.CharField(blank=True, max_length=100, null=True, verbose_name='AdCreationStatus')),
            ],
        ),
        migrations.CreateModel(
            name='CustomerFbAdCreativesCreationData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adcreative_field_message', models.CharField(blank=True, max_length=100, null=True, verbose_name='AdMessage')),
                ('adcreative_field_link', models.CharField(blank=True, max_length=100, null=True, verbose_name='AdURL')),
                ('adcreative_field_caption', models.CharField(blank=True, max_length=100, null=True, verbose_name='AdText')),
                ('adcreative_field_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='AdCreativeName')),
            ],
        ),
        migrations.CreateModel(
            name='CustomerFbAdSetCreationData',
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
            ],
        ),
        migrations.CreateModel(
            name='CustomerFbCampaignCreationData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('campaign_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='CampaignName')),
                ('campaign_objective', models.CharField(default='Campaign.Objective.link_clicks', max_length=100, null=True, verbose_name='CampaigObjective')),
                ('campaign_starting_status', models.CharField(default='Campaign.Status.paused', max_length=100, null=True, verbose_name='CampaigStatus')),
                ('customeraccount', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_galgo.CustomerAccountsFb')),
            ],
        ),
        migrations.DeleteModel(
            name='CustomerAdsCreationData',
        ),
        migrations.AddField(
            model_name='customerfbadsetcreationdata',
            name='campaign',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_galgo.CustomerFbCampaignCreationData'),
        ),
        migrations.AddField(
            model_name='customerfbadcreativescreationdata',
            name='adset',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_galgo.CustomerFbAdSetCreationData'),
        ),
        migrations.AddField(
            model_name='customerfbadcreationdata',
            name='adcreative',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_galgo.CustomerFbAdCreativesCreationData'),
        ),
    ]

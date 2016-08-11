#!/usr/bin/python
# coding: utf-8
from __future__ import unicode_literals

from django.db import models
from app_sancho.models import Customer

# Session initialization
class FbAccounts(models.Model):
    class Meta:
        verbose_name = "Cuenta de Facebook"
        verbose_name_plural = "Cuentas de Facebook"
    customer_app_id = models.CharField(null=True, blank = True, verbose_name = 'FbId')
    customer_app_secret = models.CharField(null=True, blank = True, verbose_name = 'FbSecret')
    customer_act_id = models.CharField(null=True, blank = True, verbose_name = 'AcounttId')
    customer_page_id = models.CharField(null=True, blank = True, verbose_name = 'PageId')
    customer_app_access_token = models.CharField(null=True, blank = True, verbose_name = 'FbSecretToken')

# Campaign and Ad Creation
class FbCampaign(models.Model):
    class Meta:
        verbose_name = "Campaña de Facebook"
        verbose_name_plural = "Campañas de Facebook"
    customeraccount = models.ForeignKey(FbAccounts, null=True)
    #Campaign models
    name = models.CharField(max_length = 100, null=True, blank = True, verbose_name = 'CampaignName')
    objective = models.CharField(max_length = 100, null=True, default='Campaign.Objective.link_clicks', verbose_name = 'CampaigObjective')
    starting_status = models.CharField(max_length = 400, null=True, default='Campaign.Status.paused', verbose_name = 'CampaigStatus')

class FbAdSet(models.Model):
    class Meta:
        verbose_name = "Set de Anuncios"
        verbose_name_plural = "Sets de Anuncios"
    campaign = models.ForeignKey(FbCampaign)
    #Targeting models
    target_audience_type_term = models.CharField(max_length = 100, null=True, blank = True, verbose_name = 'q')
    target_audience_search_type = models.CharField(max_length = 100, null=True, blank = True, verbose_name = 'type')

    geo_locations_countries = models.CharField(max_length = 100, null=True, blank = True, verbose_name = 'GeoLocationCountry')
    age_min = models.IntegerField(null=True, blank = True, verbose_name = 'age_min')
    age_max = models.IntegerField(null=True, blank = True, verbose_name = 'age_max')

    # Budget, Billing, Optimization and Duration models for AdSets
    adset_field_name = models.CharField(max_length = 100, null=True, blank = True, verbose_name = 'AdSetName')
    adset_field_daily_budget = models.IntegerField(null=True, blank = True, verbose_name = 'DailyBudget')
    adset_filed_billing_event = models.CharField(max_length = 100, null=True, default='AdSet.BillingEvent.impressions', verbose_name = 'Billing')
    adset_field_optimization_goal = models.CharField(max_length = 100, null=True, blank = True, verbose_name = 'AdSetOptimizationGoal')
    adset_field_bid_amount = models.IntegerField(null=True, blank = True, verbose_name = 'IntegerField')

class FbAdCreatives(models.Model):
    class Meta:
        verbose_name = "Creativo Facebook"
        verbose_name_plural = "Creativos Facebook"
    adset = models.ForeignKey(FbAdSet)
    #Images path
    #AdCreatives
    adcreative_field_message = models.CharField(max_length = 100, null=True, blank = True, verbose_name = 'AdMessage')
    adcreative_field_link = models.CharField(max_length = 100, null=True, blank = True, verbose_name = 'AdURL')
    adcreative_field_caption = models.CharField(max_length = 100, null=True, blank = True, verbose_name = 'AdText')

    adcreative_field_name = models.CharField(max_length = 100, null=True, blank = True, verbose_name = 'AdCreativeName')

class FbAd(models.Model):
    class Meta:
        verbose_name = "Anuncio de Facebook"
        verbose_name_plural = "Anuncios de Facebook"
    adcreative = models.ForeignKey(FbAdCreatives)
    #Actual Ad
    ad_field_name = models.CharField(max_length = 100, null=True, blank = True, verbose_name = 'AdName')
    ad_field_status = models.CharField(max_length = 100, null=True, blank = True, verbose_name = 'AdCreationStatus')

# Reporting
class CustomerAccountDataFb(models.Model):
    customer_account_amount_spent_fb = models.IntegerField(null=True, blank = True, verbose_name = 'CustomerAmountSpentFb')

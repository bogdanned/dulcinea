from __future__ import unicode_literals

from django.db import models

# Session initialization
class CustomerAccountsFb(models.Model):
    customer_app_id = models.IntegerField(null=True, blank = True, verbose_name = 'FbId')
    customer_app_secret = models.IntegerField(null=True, blank = True, verbose_name = 'FbSecret')
    customer_act_id = models.IntegerField(null=True, blank = True, verbose_name = 'AcounttId')
    customer_page_id = models.IntegerField(null=True, blank = True, verbose_name = 'PageId')
    customer_app_access_token = models.IntegerField(null=True, blank = True, verbose_name = 'FbSecretToken')

# Campaign and Ad Creation
class CustomerFbCampaignCreationData(models.Model):
    customeraccount = models.ForeignKey(CustomerAccountsFb)
    #Campaign models
    campaign_name = models.CharField(max_length = 100, null=True, blank = True, verbose_name = 'CampaignName')
    campaign_objective = models.CharField(max_length = 100, null=True, default='Campaign.Objective.link_clicks', verbose_name = 'CampaigObjective')
    campaign_starting_status = models.CharField(max_length = 100, null=True, default='Campaign.Status.paused', verbose_name = 'CampaigStatus')

class CustomerFbAdSetCreationData(models.Model):
    campaign = models.ForeignKey(CustomerFbCampaignCreationData)
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

class CustomerFbAdCreativesCreationData(models.Model):
    adset = models.ForeignKey(CustomerFbAdSetCreationData)
    #Images path
    #AdCreatives
    adcreative_field_message = models.CharField(max_length = 100, null=True, blank = True, verbose_name = 'AdMessage')
    adcreative_field_link = models.CharField(max_length = 100, null=True, blank = True, verbose_name = 'AdURL')
    adcreative_field_caption = models.CharField(max_length = 100, null=True, blank = True, verbose_name = 'AdText')

    adcreative_field_name = models.CharField(max_length = 100, null=True, blank = True, verbose_name = 'AdCreativeName')

class CustomerFbAdCreationData(models.Model):
    adcreative = models.ForeignKey(CustomerFbAdCreativesCreationData)
    #Actual Ad
    ad_field_name = models.CharField(max_length = 100, null=True, blank = True, verbose_name = 'AdName')
    ad_field_status = models.CharField(max_length = 100, null=True, blank = True, verbose_name = 'AdCreationStatus')

# Reporting
class CustomerAccountDataFb(models.Model):
    customer_account_amount_spent_fb = models.IntegerField(null=True, blank = True, verbose_name = 'CustomerAmountSpentFb')

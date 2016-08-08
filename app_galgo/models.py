from __future__ import unicode_literals

from django.db import models


#Customer objects


# Reporting
class CustomerAccountsFb(models.Model):
    customer_app_id = models.IntegerField(null=True, blank = True, verbose_name = 'FbId')
    customer_app_secret = models.IntegerField(null=True, blank = True, verbose_name = 'FbSecret')
    customer_app_access_token = models.IntegerField(null=True, blank = True, verbose_name = 'FbSecret')

class CustomerAccountDataFb(models.Model):
    customer_account_amount_spent_fb = models.IntegerField(null=True, blank = True, verbose_name = 'CustomerAmountSpentFb')

# AdCreation
class CustomerAdsCreationData(models.Model):
    campaign_name = models.CharField(max_length = 100, null=True, blank = True, verbose_name = 'CampaignName')
    ad_title = models.CharField(max_length = 100, null=True, blank = True, verbose_name = 'AdTitle')
    ad_body = models.CharField(max_length = 100, null=True, blank = True, verbose_name = 'AdBody')
    ad_url = models.CharField(max_length = 100, null=True, blank = True, verbose_name = 'AdUrl')
    ad_image_paths = models.CharField(max_length = 100, null=True, blank = True, verbose_name = 'AdImagePaths')
    ad_bid_type = models.CharField(max_length = 100, null=True, blank = True, verbose_name = 'BidType')
    ad_bid_info = models.CharField(max_length = 100, null=True, blank = True, verbose_name = 'BidInfo')
    ad_daily_budget = models.IntegerField(null=True, blank = True, verbose_name = 'DailyBudget')
    age_min = models.IntegerField(null=True, blank = True, verbose_name = 'AgeMin')
    age_max = models.IntegerField(null=True, blank = True, verbose_name = 'AgeMax')
    paused = models.CharField(max_length = 100, null=True, blank = True, verbose_name = 'Paused')

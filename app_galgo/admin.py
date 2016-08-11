from django.contrib import admin

from models import *

# Register your models here.

class FbAccountCampaign(admin.TabularInline):
    model = FbCampaign
    fk_name = "customeraccount"

class FbAccountsAdmin(admin.ModelAdmin):
    model = FbAccounts
    inlines = [
        FbAccountCampaign,
    ]

class CampaignFbAdSet(admin.TabularInline):
    model = FbAdSet
    fk_name = "campaign"

class FbCampaignAdmin(admin.ModelAdmin):
    model = FbCampaign
    list_display = ['campaign_name','campaign_objective','campaign_starting_status']
    list_filter = ['campaign_objective','campaign_starting_status']
    search_fields = ['campaign_name']
    inlines = [
        CampaignFbAdSet,
    ]

admin.site.register(FbAccounts, FbAccountsAdmin)
admin.site.register(FbCampaign, FbCampaignAdmin)
admin.site.register(FbAdSet)
admin.site.register(FbAdCreatives)
admin.site.register(FbAd)

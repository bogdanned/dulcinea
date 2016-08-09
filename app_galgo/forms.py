from django import forms


class FbCampaignForm(forms.Form):
    fb_campaign_name = forms.CharField(label='Campaign Name', max_length=100)

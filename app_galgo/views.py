from django.shortcuts import render

from facebookads import objects
from facebookads.objects import *
from facebookads.objects import (
    AdAccount,
    Ad,
    AdSet,
)
from facebookads.adobjects.adaccount import AdAccount

from models import *

from facebookads import FacebookSession
from facebookads import FacebookAdsApi
from utils import ad_creation_utils
import json
import os

# Creating the forms
from django.http import HttpResponseRedirect
from .forms import FbCampaignForm

# Creating a campaign remade
import time
import datetime
from facebookads.adobjects.campaign import Campaign
from facebookads.adobjects.targetingsearch import TargetingSearch
from facebookads.adobjects.targeting import Targeting
from facebookads.adobjects.adset import AdSet
from facebookads.adobjects.adimage import AdImage
from facebookads.adobjects.adcreative import AdCreative
from facebookads.adobjects.adcreativelinkdata import AdCreativeLinkData
from facebookads.adobjects.adcreativeobjectstoryspec import AdCreativeObjectStorySpec
from facebookads.adobjects.ad import Ad


def GalgoFbLogin(request):
    context = {}
    return render(request, 'login.html', context)

def GalgoGetFbCampaignRequirements(request):
     # if this is a POST request we need to process the form data
     if request.method == 'POST':
         # create a form instance and populate it with data from the request:
         form = FbCampaignForm(request.POST)
         # check whether it's valid:
         if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/create')
     # if a GET (or any other method) we'll create a blank form
     else:
         form = FbCampaignForm()

     return render(request, 'requirements.html', {'form': form})



def GalgoFbCampaignCreation(request):
    this_dir = os.path.dirname(__file__)
    config_filename = os.path.join(this_dir, 'utils', 'config.json')

    config_file = open(config_filename)
    config = json.load(config_file)
    config_file.close()
    print('///--- ACESS CONFIGURATION: ',config, ' ---///')

    ### Login to facebook and initiate the API
    session = FacebookSession(
        config['app_id'],
        config['app_secret'],
        config['access_token'],
    )
    api = FacebookAdsApi(session)
    print('///--- SESSION INITIALIZATION: OK ---///')

    FacebookAdsApi.set_default_api(api)

    # Creating Campaign with basic parameters

    campaign = Campaign(parent_id=config['act_id'])
    campaign.update({
        Campaign.Field.name: 'My first Campaign',
        Campaign.Field.objective: Campaign.Objective.link_clicks,
    })
    print('///--- CAMPAIGN PARAMETERS SETTINGS IMPLEMENTATION: OK ---///')
    campaign_id = Campaign.Field.id
    print(campaign_id, Campaign.Field.name)
    campaign.remote_create(params={
        'status': Campaign.Status.paused,
    })
    print campaign

    # Searching target audiences inside facebook
    params = {
        'q': 'real madrid baloncesto',
        'type': 'adinterest',
    }

    resp = TargetingSearch.search(params=params)
    print('///--- TARGET AUDIENCE SEARCH: OK ---///')
    print(resp)

    # Creating a sample targeting out of our results
    time.sleep(1)

    targeting = {'geo_locations':{
      'countries': ['US'],
    },
    'age_min':20,
    'age_max':24,
    'flexible_spec': [
      {
        'behaviors':[{'id':6002714895372,'name':'All travelers'},],
        'interests':[
          {'id':6003107902433,'name':'Association football (Soccer)'},
          {'id':6003139266461, 'name': 'Movies'},],
      },
      {
        'life_events':[{'id': 6002714398172, 'name': 'Newlywed (1 year)'}],
        'interests':[{'id':6003020834693,'name':'Music'},],
      },
    ],
    'exclusions': {
      'relationship_statuses':[1,3],
      'life_events':[{'id':6003054185372,'name':'Recently moved'},],
    },
    }
    print('///--- SAMPLE TARGETING CREATION: OK ---///')
    print(targeting)

    # Defining Budget, Billing, Optimization and Duration
    today = datetime.date.today()
    start_time = str(today + datetime.timedelta(weeks=6))
    end_time = str(today + datetime.timedelta(weeks=9))

    adset = AdSet(parent_id=config['act_id'])
    adset.update({
        AdSet.Field.name: 'My Ad Set',
        AdSet.Field.campaign_id: campaign[Campaign.Field.id],
        AdSet.Field.daily_budget: 500,
        AdSet.Field.billing_event: AdSet.BillingEvent.impressions,
        AdSet.Field.optimization_goal: AdSet.OptimizationGoal.reach,
        AdSet.Field.bid_amount: 20,
        AdSet.Field.targeting: targeting,
        AdSet.Field.start_time: start_time,
        AdSet.Field.end_time: end_time,
    })

    adset.remote_create(params={
        'status': AdSet.Status.paused,
    })

    print('///--- ADSET CREATION: OK ---///')
    print(adset)

    account = AdAccount(config['act_id'])
    images = account.get_ad_images()
    print(images)
    time.sleep(30)
    # Creating AdImage from Image file
    image = AdImage(parent_id=config['act_id'])
    image[AdImage.Field.filename] = os.path.join(this_dir, 'images', 'big_bike.jpg')
    image.remote_create()

    # Output the image hash
    print(image[AdImage.Field.hash])
    print('Fuck yeah')

    image_hash = image[AdImage.Field.hash]
    page_id = config['page_id']


    # Creating AdCreative
    link_data = AdCreativeLinkData()
    link_data[AdCreativeLinkData.Field.message] = 'try it out'
    link_data[AdCreativeLinkData.Field.link] = 'www.instavets.com'
    link_data[AdCreativeLinkData.Field.caption] = 'My caption'
    link_data[AdCreativeLinkData.Field.image_hash] = image_hash

    object_story_spec = AdCreativeObjectStorySpec()
    object_story_spec[AdCreativeObjectStorySpec.Field.page_id] = page_id
    object_story_spec[AdCreativeObjectStorySpec.Field.link_data] = link_data

    creative = AdCreative(parent_id=config['act_id'])
    creative[AdCreative.Field.name] = 'Ad Creative for link Ad'
    creative[AdCreative.Field.object_story_spec] = object_story_spec
    creative.remote_create()

    print(creative)

    print(image[AdImage.Field.hash])
    print('Rocket Maverickssss')
    print(adset[AdSet.Field.id])
    time.sleep(15)
    adset_id = adset[AdSet.Field.id]
    creative_id = creative[AdCreative.Field.id]

    # Creating the actual ad
    ad = Ad(parent_id = config['act_id'])
    ad[Ad.Field.name] = 'My Ad'
    ad[Ad.Field.adset_id] = adset_id
    ad[Ad.Field.creative] = {
        'creative_id': creative_id
    }
    ad.remote_create(params={
        'status': Ad.Status.paused,
    })
    print(ad)

    context = {
    }
    return render(request, 'galgo_thanks.html', context)

# Create your views here.
def GalgoApiAccesToken(request):
    if request.method == "POST":
        data = request.POST
        #1. Get data
        access_token = data.__getitem__('access_token')
        account = CustomerAccountsFb.objects.get(pk=1)

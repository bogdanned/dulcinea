from django.conf.urls import include, url
import views


urlpatterns = [
    url(r'^main$', views.GalgoGetFbCampaignRequirements, name='GalgoFbCampaignDefinition'),
    url(r'^create$', views.GalgoFbCampaignCreation, name='GalgoFbCampaignCreation'),
    url(r'^login$', views.GalgoFbLogin, name='GalgoLogin'),
    url(r'^login/api/access_token$', views.GalgoApiAccesToken, name='api_access_token'),
    url(r'^insights$', views.GalgoInsightsReporting, name='GalgoFbInsights'),
]

from django.conf.urls import include, url
import views


urlpatterns = [
    url(r'^products_view/$', views.CustomerGeneralView, name='customer_view'),
    url(r'^products_update/$', views.CustomerProductsUpdate, name='products_update'),
]

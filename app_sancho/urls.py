from django.conf.urls import include, url
import views



urlpatterns = [
    url(r'^$', views.SanchoAdminDashboard, name='sancho_admin_dashboard'),
    url(r'^customer_view/(?P<customer_pk>\d+)/$', views.CustomerGeneralView, name='customer_view'),
    url(r'^products_create/(?P<customer_pk>\d+)/$', views.CustomerProductsCreate, name='products_create'),
    url(r'^products_update/(?P<customer_pk>\d+)/$', views.CustomerProductsUpdate, name='products_update'),
    url(r'^products_view/(?P<customer_pk>\d+)/$', views.CustomerProductsView, name='products_view'),

]

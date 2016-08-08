from django.conf.urls import include, url
import views



urlpatterns = [
    url(r'^$', views.SanchoAdminDashboard, name='sancho_admin_dashboard'),
    url(r'^test/$', views.MultiThreadingTest, name='threading_test'),
    url(r'^products_view/(?P<pk>\d+)/$', views.CustomerGeneralView, name='customer_view'),
    url(r'^products_update/(?P<customer_pk>\d+)/$', views.CustomerProductsUpdate, name='products_update'),
]

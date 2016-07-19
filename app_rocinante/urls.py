from django.conf.urls import include, url
import views


urlpatterns = [
    url(r'^connection/$', views.ConnectionTest, name='db_conection'),
]

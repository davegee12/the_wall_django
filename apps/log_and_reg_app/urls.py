from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^create$', views.create_user),
    url(r'^success$', views.success),
    url(r'^login$', views.login),
    url(r'^log_out$', views.log_out),
]
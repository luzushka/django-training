from django.conf.urls import include, url
from django.contrib import admin
from . import views
urlpatterns = [
    # /polls/
    url(r'^$',views.index,name='index'),

    # /music/71/
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),
    ]

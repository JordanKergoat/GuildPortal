__author__ = 'Jordan'

from django.conf.urls import patterns, include, url
from django.contrib import admin
from .views import index
from Portal.views import index as portal_index
from Forum.views import index as forum_index

urlpatterns = patterns('',
    url(r'^$', index, name='super_portal_index'),
    url(r'^forum/$', forum_index, name='portal_index'),
    url(r'^(?P<portal_name>\w+[\- ]*\w+)/$', portal_index, name='portal_index'),
)
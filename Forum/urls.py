__author__ = 'Jordan'

from django.conf.urls import patterns, include, url
from django.contrib import admin
from .views import index

urlpatterns = patterns('',
    url(r'^$', index, name='super_portal_index'),
)
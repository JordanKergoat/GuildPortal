__author__ = 'Jordan'

from django.conf.urls import patterns, include, url
from django.contrib import admin
from .views import index, IndexListCategoryView

urlpatterns = patterns('',
    url(r'^$', IndexListCategoryView.as_view(), name='super_portal_index'),
)
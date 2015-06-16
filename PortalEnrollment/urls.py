__author__ = 'Alexandre Cloquet'


from django.conf.urls import patterns, include, url
from django.contrib import admin
from .views import EnrollementView as index
from Portal.views import index as portal_index
from Forum.views import index as forum_index

urlpatterns = patterns('',
    url(r'^$', index.as_view(), name='enrollement_index'),
                       )
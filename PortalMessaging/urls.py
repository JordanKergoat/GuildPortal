from PortalMessaging.views import IndexMessage, MessageDetails

__author__ = 'cloquet'


from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', IndexMessage.as_view(), name='message_index'),
    url(r'^(?P<message_id>[\d]+)/$', MessageDetails.as_view(), name='message_details'),
        )
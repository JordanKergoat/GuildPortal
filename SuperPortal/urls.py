__author__ = 'Jordan'

from django.conf.urls import patterns, include, url
from django.contrib import admin
from .views import index, Profile, Members
from Forum.views import index as forum_index

urlpatterns = patterns('',
    url(r'^$', index, name='super_portal_index'),
    url(r'^forum/$', forum_index, name='forum_index'),
    url(r'^profile/$', Profile.as_view(), name='profile'),
    url(r'^members/$', Members.as_view(), name='member'),

    #url(r'^(?P<portal_name>(?:\w+\s*\w+)+)/$', portal_index, name='portal_index'),
    url(r'^(?P<portal_name>(?:\w+\s*\w+)+)/', include('Portal.urls')),
)
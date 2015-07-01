__author__ = 'Jordan'

from django.conf.urls import patterns, include, url
from .views import index, Profile, Members
from Forum.views import index as forum_index

urlpatterns = patterns('',
    url(r'^$', index, name='super_portal_index'),
    url(r'^forum/$', forum_index, name='forum_index'),
    url(r'^profile/$', Profile.as_view(), name='profile'),
    url(r'^profile/(?P<pk>(?:\d+))/$', Profile.as_view(), name='profile_user'),
    url(r'^members/$', Members.as_view(), name='members'),
    url(r'^(?P<portal_name>(?:\w+[-\s*]*(\w+)*)+)/', include('Portal.urls')),
)
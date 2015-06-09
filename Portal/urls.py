__author__ = 'Alexandre Cloquet'



from django.conf.urls import patterns, include, url
from django.contrib import admin
from .views import index, news_detail
from Portal.views import index as portal_index
from Forum.views import index as forum_index

urlpatterns = patterns('',
    url(r'^$', index, name='portal_index'),
    url(r'^(?P<category>(?:\w+\s*\w+)+)/(?P<news_name>(?:\w+[ \t\n\r\f\v:]*\w+)+)/$', news_detail, name='news_detail'),
                       )
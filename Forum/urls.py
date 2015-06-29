__author__ = 'Jordan'

from django.conf.urls import patterns, include, url
from django.contrib import admin
from .views import index, IndexListCategoryView, IndexCategoryView

urlpatterns = patterns('',
    url(r'^$', IndexListCategoryView.as_view(), name='super_portal_index'),
    url(r'^(?P<category>(?:\w+[-\t\n\r\f\v:]*\w+)+)/$', IndexCategoryView.as_view(), name='category_detail_forum'),
)
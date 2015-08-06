__author__ = 'Jordan'

from django.conf.urls import patterns, include, url
from django.contrib import admin
from .views import index, IndexListCategoryView, IndexCategoryView, DetailForumView, DetailThreadView, CreateThreadView, \
    CreatePostView

urlpatterns = patterns('',
    url(r'^$', IndexListCategoryView.as_view(), name='super_portal_index'),
    url(r'^(?P<category>(?:\w+[-\t\n\r\f\v:]*\w+)+)/$', IndexCategoryView.as_view(), name='category_detail_forum'),
    url(r'^(?P<category>(?:\w+[-\t\n\r\f\v:]*\w+)+)/(?P<title>(?:\w+[-\t\n\r\f\v:]*\w+)+)/$', DetailForumView.as_view(), name='forum_detail'),
    url(r'^(?P<category>(?:\w+[-\t\n\r\f\v:]*\w+)+)/(?P<title>(?:\w+[-\t\n\r\f\v:]*\w+)+)/create/$', CreateThreadView.as_view(), name='create_thread'),
    url(r'^(?P<category>(?:\w+[-\t\n\r\f\v:]*\w+)+)/(?P<title>(?:\w+[-\t\n\r\f\v:]*\w+)+)/(?P<thread_name>(?:\w+[-\t\n\r\f\v:]*\w+)+)/$', DetailThreadView.as_view(), name='thread_detail'),
    url(r'^(?P<category>(?:\w+[-\t\n\r\f\v:]*\w+)+)/(?P<title>(?:\w+[-\t\n\r\f\v:]*\w+)+)/(?P<thread_name>(?:\w+[-\t\n\r\f\v:]*\w+)+)/new/$', CreatePostView.as_view(), name='create_post'),

)
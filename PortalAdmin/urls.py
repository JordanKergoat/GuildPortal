__author__ = 'Jordan'

from django.conf.urls import patterns, include, url
from .views import AdminIndexView, AdminMembersView, AdminUserDetailView, AdminUserUpdateView

urlpatterns = patterns('',
                       url(r'^$', AdminIndexView.as_view(), name='admin_index'),

                       url(r'^members/$', AdminMembersView.as_view(), name='admin_members'),
                       url(r'^members/(?P<pk>\d+)/details/$', AdminUserDetailView.as_view(), name='admin_user_detail'),
                       url(r'^members/(?P<pk>\d+)/update/$', AdminUserUpdateView.as_view(), name='admin_user_detail'),

                       )

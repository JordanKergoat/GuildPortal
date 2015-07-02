__author__ = 'Jordan'

from django.conf.urls import patterns, include, url
from .views import AdminIndexView

urlpatterns = patterns('',
                       url(r'^$', AdminIndexView.as_view(), name='admin_index'),
                       )

__author__ = 'Alexandre Cloquet'


from django.conf.urls import patterns, include, url
from django.contrib import admin
from .views import OpenEnrollementView, CharacterAttributesView, EnrollementView, EnrollementListView
from Portal.views import index as portal_index
from Forum.views import index as forum_index

urlpatterns = patterns('',
    url(r'^$', OpenEnrollementView.as_view(), name='enrollement_index'),
    url(r'^list_enrollement/$', EnrollementListView.as_view(), name='enrollement_list'),
    url(r'^(?P<id_application>(\d+))/$', EnrollementView.as_view(), name='enrollement'),
    url(r'^character_attributes$', CharacterAttributesView.as_view(), name='character_attributes'),
                       )
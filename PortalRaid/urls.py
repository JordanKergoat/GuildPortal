from PortalRaid.views import NewCharacterFormView, ServerListView, ListCharactersUser, DetailsCharacter,\
    DetailsCharacterFromAPI, RaidListView, RaidDetailView

__author__ = 'Alexandre Cloquet'

from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
                       url(r'^$', RaidListView.as_view(), name='index_raid'),
                       url(r'^(?P<pk>\d+)$', RaidDetailView.as_view(), name='raid_detail'),
                       url(r'^add_new_character/$', NewCharacterFormView.as_view(), name='new_character'),

                       url(r'^server_list$', ServerListView.as_view(), name='serverlist'),
                       url(r'^list_characters_user/$', ListCharactersUser.as_view(), name='list_characters_user'),
                       url(r'^detail_characters/(?P<pk>\d+)/$', DetailsCharacter.as_view(), name='detail_characters'),
                       url(r'^detail_characters_from_api$', DetailsCharacterFromAPI.as_view(), name='detail_characters_from_api'),
                       )
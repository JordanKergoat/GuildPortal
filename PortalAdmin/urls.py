__author__ = 'Jordan'

from django.conf.urls import patterns, include, url
from .views import AdminIndexView, AdminMembersView, AdminUserDetailView, AdminUserUpdateView, LastPostLastComments, \
    AdminGamesView, AdminGameUpdateView, AdminGameDetailView, AdminGameCreate, AdminGameCharactersCreate, \
    AdminPortalCreateView, AdminPortalUpdate, AdminGuildSetting

urlpatterns = patterns('',
                       url(r'^$', AdminIndexView.as_view(), name='admin_index'),
                       url(r'^guild_settings/$', AdminGuildSetting.as_view(), name='admin_guild_setting'),

                       url(r'^members/$', AdminMembersView.as_view(), name='admin_members'),
                       url(r'^members/(?P<pk>\d+)/details/$', AdminUserDetailView.as_view(), name='admin_user_detail'),
                       url(r'^members/(?P<pk>\d+)/update/$', AdminUserUpdateView.as_view(), name='admin_user_update'),
                       url(r'^members/(?P<pk>\d+)/last_post_last_comments/$', LastPostLastComments.as_view(), name='last_post_last_comments'),

                       url(r'^games/$', AdminGamesView.as_view(), name='admin_games'),
                       url(r'^games/add/$', AdminGameCreate.as_view(), name='admin_games_add'),
                       url(r'^games/(?P<pk>\d+)/details/$', AdminGameDetailView.as_view(), name='admin_game_detail'),
                       url(r'^games/(?P<pk>\d+)/update/$', AdminGameUpdateView.as_view(), name='admin_game_update'),
                       url(r'^games/(?P<pk>\d+)/character-details/$', AdminGameUpdateView.as_view(), name='admin_game_characters_details'),
                       url(r'^games/(?P<pk>\d+)/character-details/add/$', AdminGameCharactersCreate.as_view(), name='admin_game_characters_details_add'),

                       url(r'^portal/(?P<pk_game>\d+)/$', AdminPortalUpdate.as_view(), name='admin_portal'),
                       url(r'^portal/(?P<pk_game>\d+)/add/$', AdminPortalCreateView.as_view(), name='admin_portal_add'),

                       )

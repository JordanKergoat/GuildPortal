__author__ = 'Jordan'

from django.conf.urls import patterns, include, url
from .views import AdminIndexView, AdminMembersView, AdminUserDetailView, AdminUserUpdateView, LastPostLastComments, \
    AdminGamesView, AdminGameUpdateView, AdminGameDetailView, AdminGameCreate, AdminGameCharactersCreate, \
    AdminPortalCreateView, AdminPortalUpdate, AdminGuildSetting, AdminGuildSettingCreate, AdminGuildSettingEdit, \
    AdminEnrollmentNeeds, AdminDatabaseAddTable, AdminDatabaseAddEntry, AdminRaidsView, AdminRaidsAdd, \
    AdminRaidsUpdate, AdminRaidOutView, AdminSuperPortalCreate

urlpatterns = patterns('',
                       url(r'^$', AdminIndexView.as_view(), name='admin_index'),
                       url(r'^guild_settings/(?P<pk>\d+)/$', AdminGuildSetting.as_view(), name='admin_guild_setting'),
                       url(r'^guild_settings/create/$', AdminGuildSettingCreate.as_view(), name='admin_guild_setting_create'),
                       url(r'^superportal/create/$', AdminSuperPortalCreate.as_view(), name='admin_superportal_create'),
                       url(r'^guild_settings/(?P<pk>\d+)/update/$', AdminGuildSettingEdit.as_view(), name='admin_guild_setting_update'),


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

                       url(r'^games/(?P<pk_game>\d+)/database/tables/add$', AdminDatabaseAddTable.as_view(), name='admin_games_add_table'),
                       url(r'^games/(?P<pk_game>\d+)/database/tables/(?P<pk_table>\d+)/', AdminDatabaseAddEntry.as_view(), name='admin_games_add_entry'),

                       url(r'^games/(?P<pk>\d+)/enrollment/needs/$', AdminEnrollmentNeeds.as_view(), name='admin_game_enrollment_needs'),
                       url(r'^games/(?P<pk>\d+)/enrollment/ongoing/$', AdminGameUpdateView.as_view(), name='admin_game_enrollment_ongoing'),

                       url(r'^portal/(?P<pk_game>\d+)/$', AdminPortalUpdate.as_view(), name='admin_portal'),
                       url(r'^portal/(?P<pk_game>\d+)/add/$', AdminPortalCreateView.as_view(), name='admin_portal_add'),


                       url(r'^games/(?P<pk_game>\d+)/raids/$', AdminRaidsView.as_view(), name='admin_raids'),
                       url(r'^games/(?P<pk_game>\d+)/raids/add/$', AdminRaidsAdd.as_view(), name='admin_raid_add'),
                       url(r'^games/(?P<pk_game>\d+)/raids/(?P<pk_raid>\d+)/update/$', AdminRaidsUpdate.as_view(), name='admin_raid_update'),
                       url(r'^games/(?P<pk_game>\d+)/raids/(?P<pk_raid>\d+)/details/$', AdminPortalCreateView.as_view(), name='admin_raid_details'),

                       url(r'^games/(?P<pk_game>\d+)/raids_out/$', AdminRaidOutView.as_view(), name='admin_raids_out'),
                       url(r'^games/(?P<pk_game>\d+)/raids_out/add/$', AdminPortalCreateView.as_view(), name='admin_raid_out_add'),
                       url(r'^games/(?P<pk_game>\d+)/raids_out/(?P<pk_raid>\d+)/update/$', AdminPortalCreateView.as_view(), name='admin_raid_out_update'),
                       url(r'^games/(?P<pk_game>\d+)/raids_out/(?P<pk_raid>\d+)/details/$', AdminPortalCreateView.as_view(), name='admin_raid_out_details'),

                       url(r'^games/(?P<pk_game>\d+)/news/$', AdminPortalCreateView.as_view(), name='admin_news'),
                       url(r'^games/(?P<pk_game>\d+)/news/add/$', AdminPortalCreateView.as_view(), name='admin_news_add'),
                       url(r'^games/(?P<pk_game>\d+)/news/(?P<pk_raid>\d+)/update/$', AdminPortalCreateView.as_view(), name='admin_news_update'),
                       url(r'^games/(?P<pk_game>\d+)/news/(?P<pk_raid>\d+)/details/$', AdminPortalCreateView.as_view(), name='admin_news_details'),

                       )

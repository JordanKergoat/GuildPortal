from django.views.decorators.http import require_POST

__author__ = 'Alexandre Cloquet'

from django.conf.urls import patterns, include, url
from django.contrib import admin
from .views import OpenEnrollementView, CharacterAttributesView, EnrollementView, EnrollementListView, \
    EnrollmentDetailView, \
    CommentEnrollmentFormView, EnrollmentDetail, voteUp, voteDown, redirect_to_bnet, tmp
from Portal.views import index as portal_index
from Forum.views import index as forum_index

urlpatterns = patterns('',
                       url(r'^$', OpenEnrollementView.as_view(), name='enrollement_index'),
                       url(r'^list_enrollement/$', EnrollementListView.as_view(), name='enrollement_list'),

                       url(r'^test/$', redirect_to_bnet, name='test_battlenet'),
                       url(r'^tmp/$', tmp, name='test_battlenet'),

                       url(r'^detail/(?P<pk>\d+)/$', EnrollmentDetail.as_view(), name='enrollment_detail'),
                       url(r'^detail/(?P<pk>\d+)/comment/$', require_POST(CommentEnrollmentFormView.as_view()),
                           name='enrollment_detail_comment'),
                       url(r'^detail/(?P<pk>\d+)/voteup/$', voteUp, name='voteup'),
                       url(r'^detail/(?P<pk>\d+)/votedown/$', voteDown, name='votedown'),

                       url(r'^(?P<id_application>(\d+))/$', EnrollementView.as_view(), name='enrollement_application'),
                       url(r'^character_attributes$', CharacterAttributesView.as_view(), name='character_attributes'),
                       )

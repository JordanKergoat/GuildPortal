__author__ = 'Alexandre Cloquet'



from django.conf.urls import patterns, url
from .views import index, NewsDetail

urlpatterns = patterns(
    '',
    url(r'^$', index, name='portal_index'),
    url(r'^(?P<category>(?:\w+\s*\w+)+)/(?P<news_name>(?:\w+[-\t\n\r\f\v:]*\w+)+)/$', NewsDetail.as_view(), name='news_detail'),
)
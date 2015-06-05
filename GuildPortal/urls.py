from django.conf.urls import patterns, include, url
from django.contrib import admin
from Portal.views import index
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'GuildPortal.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^forum/', include('Forum.urls')),
    url(r'', include('SuperPortal.urls')),
)

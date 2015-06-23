from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from Portal.views import index

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'GuildPortal.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^forum/', include('Forum.urls')),
    url(r'^message/', include('PortalMessaging.urls')),
    url(r'^raid/', include('PortalRaid.urls')),
    url(r'^recrutement/', include('PortalEnrollment.urls')),
    url(r'', include('SuperPortal.urls')),
)


if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )

from django.conf import settings
if settings.DEBUG:
    urlpatterns += patterns('',

    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT,
    }),
    url(r'^media/news/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT,
    }),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.STATIC_ROOT,
    }),
)

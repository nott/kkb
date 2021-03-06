from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.contrib import admin


admin.autodiscover()

handler500 = 'cinemaclubs.views.error500'

if settings.DEBUG:
    urlpatterns = patterns('', (r'^site_media/media/(?P<path>.*)$',
                                'django.views.static.serve',
                                {'document_root': settings.MEDIA_ROOT}),)
    urlpatterns += patterns('', (r'^site_media/static/(?P<path>.*)$',
                                 'django.views.static.serve',
                                 {'document_root': settings.STATIC_ROOT}),)
else:
    urlpatterns = []

urlpatterns += patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^soc/login/(?P<backend>[^/]+)/$',
        'cinemaclubs.views.kkb_socialauth_begin',
        name='kkb_socialauth_begin'),
    url(r'^auth-error/$', 'cinemaclubs.views.auth_error', name='error'),
    url(r'^soc/', include('social_auth.urls')),
    url(r'^feedback/', include('feedback.urls')),

    url(r'^$', 'cinemaclubs.views.home', name='home'),
    url(r'^minska/$', 'cinemaclubs.views.minsk', name='minsk'),

    url(r'^comments/', include('django.contrib.comments.urls')),
    url(r'^blog/', include('blog.urls')),
    url(r'^logout/$', 'cinemaclubs.views.logout', name='logout'),
    url(r'^(?P<url>[\w\d/]*)logout/',
        'cinemaclubs.views.anything_logout',
        name='anything_logout'),

    url(r'^spis/$',
        'cinemaclubs.views.cinemaclub_list',
        name='cinemaclub_list'),
    url(r'^calendar/$',
        'cinemaclubs.views.calendar',
        name='calendar'),
    url(r'^calendar/rss/$',
        'cinemaclubs.feeds.calendar',
        name='calendar_rss'),

    # url(r'^event/add/',
    #     'cinemaclubs.views.cinemaclubevent_add',
    #     name='cinemaclubevent_add'),
    # url(r'^event/(?P<event_id>\d+)/edit_poster/',
    #     'cinemaclubs.views.cinemaclubevent_edit_poster',
    #     name='cinemaclubevent_edit_poster'),
    # url(r'^event/(?P<event_id>\d+)/crop_poster/(?P<tmp_img_id>\d+)/',
    #     'cinemaclubs.views.cinemaclubevent_crop_poster',
    #     name='cinemaclubevent_crop_poster'),

    url(r'^e/(?P<event_id>\d+)/', 'cinemaclubs.views.someevent',
        name='someevent'),
    url(r'^(?P<cinemaclub_slug>\w+)/(?P<event_id>\d+)/',
        'cinemaclubs.views.cinemaclubevent', name='cinemaclubevent'),

    url(r'^(?P<cinemaclub_slug>\w+)/$', 'cinemaclubs.views.cinemaclub_about',
        name='cinemaclub_about'),

)

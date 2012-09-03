from django.conf.urls import patterns, include, url
from django.views.generic.simple import redirect_to

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'codecamp.views.home', name='home'),
    # url(r'^codecamp/', include('codecamp.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    # Sessions
    url(r'^sessions/$', 'codecamp.views.sessions_index'),
    (r'^sessions$', redirect_to, {'url': '/sessions/'}),
    url(r'^sessions/(?P<slug>[-\w\d]+),(?P<id>\d+)/$', 'codecamp.views.session_detail', name='session_detail'),
    (r'^submit$', redirect_to, {'url': '/sessions/submit'}),
    url(r'^sessions/submit$', 'codecamp.views.session_submit', name='session_submit'),
    # Speakers
    url(r'^speakers/$', 'codecamp.views.speakers_index'),
    (r'^speakers$', redirect_to, {'url': '/speakers/'}),
    url(r'^speakers/(?P<slug>[-\w\d]+),(?P<id>\d+)/$', 'codecamp.views.speaker_detail', name='speaker_detail'),
    (r'register$', redirect_to, {'url': 'http://www.eventbrite.com/event/4216204782/es2?utm_source=sdcc_redir'}),
    # Haystack
    (r'^search/', include('haystack.urls')),
    (r'^search$', redirect_to, {'url': '/search/'}),
    # Flatpages
    (r'', include('django.contrib.flatpages.urls')),

)

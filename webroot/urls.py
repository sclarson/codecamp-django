from django.conf.urls import patterns, include, url
from django.views.generic.simple import redirect_to
from codecamp.feeds import SessionsFeedAtom, SessionsFeedRSS2
from tastypie.api import Api
from codecamp.api.resources import SessionResource

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
import codecamp

admin.autodiscover()

v1_api = Api(api_name='v1')
v1_api.register(SessionResource())

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'codecamp.views.home', name='home'),
    # url(r'^codecamp/', include('codecamp.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    # Sessions
    (r'^sessions$', redirect_to, {'url': '/sessions/'}), 
    (r'sessions/', include('codecamp.urls.sessions')),
    (r'^submit$', redirect_to, {'url': '/sessions/submit'}),
    url(r'^sessions/submit$', 'codecamp.views.session_submit', name='session_submit'),
    (r'^sessions/atom$', SessionsFeedAtom()),
    (r'^sessions/rss$', SessionsFeedRSS2()),
    # Speakers
    (r'^speakers$', redirect_to, {'url': '/speakers/'}),
    (r'^speakers/', include('codecamp.urls.speakers')),
    (r'register$', redirect_to, {'url': 'http://www.eventbrite.com/event/4216204782/es2?utm_source=sdcc_redir'}),
    # Haystack
    (r'^search/', include('haystack.urls')),
    (r'^search$', redirect_to, {'url': '/search/'}),
    # API
    (r'^api/', include(v1_api.urls)),
    # Flatpages
    (r'', include('django.contrib.flatpages.urls')),

)

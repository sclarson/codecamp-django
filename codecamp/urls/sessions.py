from django.conf.urls import *

from codecamp.models import Session


urlpatterns = patterns('',
    url(r'^$', 'codecamp.views.sessions_index'),
    url(r'^(?P<year>\d{4})/$','codecamp.views.session_archive', name='session_archive'),
    url(r'^(?P<year>\d{4})/(?P<slug>[-\w\d]+),(?P<id>\d+)/$','codecamp.views.session_detail', name='session_slug'),
    url(r'^(?P<slug>[-\w\d]+),(?P<id>\d+)/$', 'codecamp.views.session_detail', name='session_detail'),
)

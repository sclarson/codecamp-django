from django.conf.urls.defaults import *

from codecamp.models import Session


urlpatterns = patterns('',
    url(r'^$', 'codecamp.views.sessions_index'),
    url(r'^(?P<slug>[-\w\d]+),(?P<id>\d+)/$', 'codecamp.views.session_detail', name='session_detail'),
)
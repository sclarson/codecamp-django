from django.conf.urls.defaults import *

from codecamp.models import Session


urlpatterns = patterns('',
    (r'^$', 'django.views.generic.list_detail.object_list',
    url(r'^sessions/(?P<slug>[-\w\d]+),(?P<id>\d+)/$','codecamp.views.session_detail', name='session_detail'),
)
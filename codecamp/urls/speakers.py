from django.conf.urls.defaults import *

from codecamp.models import Speaker


urlpatterns = patterns('',
    (r'^$', 'django.views.generic.list_detail.object_list',
    url(r'^speakers/(?P<slug>[-\w\d]+),(?P<id>\d+)/$','codecamp.views.speaker_detail', name='speaker_detail'),
)
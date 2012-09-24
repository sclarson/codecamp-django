from django.conf.urls import *
from codecamp.models import Speaker


urlpatterns = patterns('',
    url(r'^$', 'codecamp.views.speakers_index'),
    url(r'^(?P<slug>[-\w\d]+),(?P<id>\d+)/$', 'codecamp.views.speaker_detail', name='speaker_detail'),
)

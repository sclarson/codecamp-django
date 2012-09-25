from django.conf.urls import *
from codecamp.models import SubmittedSession


urlpatterns = patterns('',
    url(r'^$', 'codecamp.views.submittedsession_index'),
)

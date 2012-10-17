from tastypie import fields
from tastypie.authentication import ApiKeyAuthentication
from tastypie.authorization import Authorization
from tastypie.resources import ModelResource
from codecamp.models import Session, Speaker

class SpeakerResource(ModelResource):
    session = fields.ToManyField('codecamp.api.resources.SessionResource', 'session_set', related_name='session')
    class Meta:
        queryset = Speaker.objects.all()
        allowed_methods = ['get']
        authorization = Authorization()

class SessionResource(ModelResource):
    speaker = fields.ManyToManyField(SpeakerResource, 'speakers')
    class Meta:
        queryset = Session.objects.all()
        allowed_methods = ['get']
        authorization = Authorization()

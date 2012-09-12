from tastypie.resources import ModelResource
from codecamp.models import Session

class SessionResource(ModelResource):
    class Meta:
        queryset = Session.objects.all()
        allowed_methods = ['get']
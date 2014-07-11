from tastypie.resources import ModelResource
from models import FacebookUser

class FacebookUserResource(ModelResource):
    class Meta:
        queryset = FacebookUser.objects.all()
        resource_name = 'person'


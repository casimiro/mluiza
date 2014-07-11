from tastypie.resources import ModelResource
from models import FacebookUser

import urllib2
import ast

class FacebookUserResource(ModelResource):
    class Meta:
        queryset = FacebookUser.objects.all()
        resource_name = 'person'

    def obj_create(self, bundle, **kwargs):
        content = urllib2.urlopen("https://graph.facebook.com/%s" % kwargs['facebookId']).read()
        vals = ast.literal_eval(content)
        
        for key in ['username', 'name', 'gender']:
            kwargs[key] = vals[key]

        kwargs['facebook_id'] = kwargs['facebookId']

        return super(FacebookUserResource, self).obj_create(bundle, **kwargs)

    def deserialize(self, request, data, format='application/json'):
        print "Deserializing..."
        print format
        if format == 'multipart/form-data':
            print data

        return super(FacebookUserResource, self).deserialize(request, data, format)

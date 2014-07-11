from models import FacebookUser
from rest_framework import serializers

import urllib2
import ast

class FacebookUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FacebookUser
        fields = ['username', 'facebookId', 'name', 'gender']


    def from_native(self, data, files):
        '''
        Overriding the deserialization to add data
        collected from Facebook graph api.
        '''
        content = urllib2.urlopen("https://graph.facebook.com/%s" % data['facebookId']).read()
        vals = ast.literal_eval(content)
        print vals

        for key in ['username', 'name', 'gender']:
            data[key] = vals[key]

        data['facebookId'] = vals['id']

        return super(FacebookUserSerializer, self).from_native(data, files)



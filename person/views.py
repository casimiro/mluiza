from person.models import FacebookUser
from rest_framework import viewsets
from person.serializers import FacebookUserSerializer
from rest_framework.response import Response

import logging
logger = logging.getLogger(__name__)

class FacebookUserViewSet(viewsets.ModelViewSet):
    queryset = FacebookUser.objects.all()
    serializer_class = FacebookUserSerializer

    def initial(self, request, *args, **kwargs):
        data = request.DATA
        logger.debug("[{0}] {1} {2} {3}".format(self.__class__.__name__, request.method, request.path, data))

        super(FacebookUserViewSet, self).initial(request, args, kwargs)

    def list(self, request, *args, **kwargs):
        '''
        Overriding default list in order to parse
        the url param limit and thus limit the results
        '''
        
        if 'limit' in request.QUERY_PARAMS.keys():
            limit = request.QUERY_PARAMS['limit'][0]
            self.object_list = self.filter_queryset(self.get_queryset())[:limit]
        else:
            self.object_list = self.filter_queryset(self.get_queryset())

        serializer = self.get_serializer(self.object_list, many=True)

        return Response(serializer.data)

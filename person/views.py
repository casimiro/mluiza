from person.models import FacebookUser
from rest_framework import viewsets
from person.serializers import FacebookUserSerializer
from rest_framework.response import Response

import logging
logger = logging.getLogger(__name__)

class FacebookUserViewSet(viewsets.ModelViewSet):
    queryset = FacebookUser.objects.all()
    serializer_class = FacebookUserSerializer

    def get(self, request, format=None):
        print request
        users = FacebookUser.objects.all()
        return Response(users)

    def initial(self, request, *args, **kwargs):
        data = request.DATA
        logger.debug("[{0}] {1} {2} {3}".format(self.__class__.__name__, request.method, request.path, data))

        super(FacebookUserViewSet, self).initial(request, args, kwargs)

    def list(self, request, *args, **kwargs):
        '''
        Overriding default list in order to parse
        the url param limit and thus limit the results
        '''

        limit = request.QUERY_PARAMS['limit'][0]

        self.object_list = self.filter_queryset(self.get_queryset())[:limit]

        # Default is to allow empty querysets.  This can be altered by setting
        # `.allow_empty = False`, to raise 404 errors on empty querysets.
        if not self.allow_empty and not self.object_list:
            warnings.warn(
                'The `allow_empty` parameter is due to be deprecated. '
                'To use `allow_empty=False` style behavior, You should override '
                '`get_queryset()` and explicitly raise a 404 on empty querysets.',
                PendingDeprecationWarning
            )
            class_name = self.__class__.__name__
            error_msg = self.empty_error % {'class_name': class_name}
            raise Http404(error_msg)

        # Switch between paginated or standard style responses
        page = self.paginate_queryset(self.object_list)
        if page is not None:
            serializer = self.get_pagination_serializer(page)
        else:
            serializer = self.get_serializer(self.object_list, many=True)

        return Response(serializer.data)

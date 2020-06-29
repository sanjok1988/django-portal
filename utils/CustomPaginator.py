from collections import OrderedDict
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.utils.urls import replace_query_param, remove_query_param


class CustomPagination(LimitOffsetPagination):
    page = 1
    default_limit = 10
    # max_limit = 50
    page_size_query_param = 'page_size'

    def get_paginated_response(self, data):
        offset = self.request.query_params.get('offset')
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'total': self.count,
            'offset': offset,
            'results': data
        })


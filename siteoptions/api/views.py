from rest_framework import generics, mixins, viewsets
from rest_framework.permissions import AllowAny

from siteoptions.api.serializers import ListOptionSerializer
from siteoptions.models import SiteOptions


class OptionsViewSet(
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    permission_classes = (AllowAny,)
    queryset = SiteOptions.objects.all()
    serializer_class = ListOptionSerializer

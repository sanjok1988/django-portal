from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny

from team.api.serializers import TeamSerializer
from team.models import Team


class TeamViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):

    permission_classes = (AllowAny,)

    queryset = Team.objects.all()
    serializer_class = TeamSerializer

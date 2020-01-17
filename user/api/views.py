from django.contrib.auth.models import User, Group

from rest_framework import viewsets, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from user.api.serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


# Retrieve list of users using class based generic list api view
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def list(self, request, *args, **kwargs):
        serializer_context = {
            'request': request,
        }
        queryset = self.get_queryset()
        serializer = UserSerializer(queryset, context=serializer_context, many=True)
        return Response(serializer.data)


# Retrieve list of users using functional based api view
@api_view(['GET'])
def get_users(request):
    serializer_context = {
        'request': request,
    }
    users = User.objects.all()
    serializer = UserSerializer(users, context=serializer_context, many=True)
    return Response(serializer.data)

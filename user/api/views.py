from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.models import User, Group, Permission
from django.shortcuts import get_object_or_404

from rest_framework import viewsets, generics, status
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from user.api.serializers import UserSerializer, GroupSerializer, PermissionSerializer


class LoginView(APIView):
    permission_classes = ()

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            return Response({"token": user.auth_token.key})
        else:
            return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)


class RegisterUserView(CreateAPIView):
    print('testing')
    # model = get_user_model()
    permission_classes = (AllowAny,)
    # serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        return Response('test')


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)#(IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


# Retrieve list of users using class based generic list api view
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

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


@api_view(['GET'])
def get_permissions(request):
    permissions = Permission.objects.all()
    serializer = PermissionSerializer(permissions, many=True)
    return Response(serializer.data)


class Permissions(viewsets.ModelViewSet):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer

    def get_user_permission(self, bundle, **kwargs):
        user_id = kwargs.get('user_id')
        user = get_object_or_404(User, id=user_id)
        permissions = user.user_permissions.all()
        serializer = self.get_serializer(permissions, many=True)
        return Response(serializer.data)

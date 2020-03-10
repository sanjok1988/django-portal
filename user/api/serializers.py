from django.contrib.auth.models import Group, User, Permission
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.serializers import ModelSerializer


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

        def create(self, validated_data):
            user = User.objects.create(
                username=validated_data['username'],
                email=validated_data['email'],
                first_name=validated_data['first_name'],
                last_name=validated_data['last_name']
            )

            user.set_password(validated_data['password'])
            user.save()

            return user


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class PermissionSerializer(ModelSerializer):
    class Meta:
        model = Permission
        fields = ('codename', 'name')


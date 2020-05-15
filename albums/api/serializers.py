from rest_framework import serializers

from albums.models import Album, Photo


class AlbumSerializer(serializers.ModelSerializer):

    class Meta:
        model = Album
        fields = ['id', 'album_name', 'slug', 'cover_photo', 'description', 'status', 'created_at']


class PhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Photo
        fields = ['id', 'album', 'title', 'photo', 'description', 'caption', 'status', 'created_at']


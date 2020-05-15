from django.core.files import File
from rest_framework import viewsets, mixins, status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from albums.api.serializers import AlbumSerializer, PhotoSerializer
from albums.models import Album, Photo


class AlbumViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    permission_classes = (AllowAny,)

    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class PhotoViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    permission_classes = (AllowAny,)

    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    #
    # def perform_create(self, serializer):
    #     serializer.save()
    #
    # def get_success_headers(self, data):
    #     try:
    #         return {'Location': str(data[api_settings.URL_FIELD_NAME])}
    #     except (TypeError, KeyError):
    #         return {}


class UploadToAlbumViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = (AllowAny,)
    serializer_class = PhotoSerializer
    queryset = Photo.objects.all()

    def create(self, request, *args, **kwargs):
        album_id = kwargs.get('id')
        # album = Album.objects.get(pk=album_id)
        # print(request.FILES)
        # print(request.data)
        # images = dict((request.data).lists())['photo[0]']
        # print(images)
        # for key, value in request.FILES.items():
        #     print(value.name, value)
        # objs = [
        #     Photo(
        #         album=album,
        #         photo=images
        #     )
        #     for key, image in request.data.items()
        # ]
        # print(objs)

        # for i, photo in enumerate(request.data):
        #     print(i,photo)
        # result = Photo.objects.bulk_create(objs=objs)
        # print(result)
        #

        request.data['album'] = album_id
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):
        queryset = Photo.objects.filter(album=kwargs.get('id')).order_by('id').reverse()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)



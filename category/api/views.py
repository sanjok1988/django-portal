from django.shortcuts import get_object_or_404
from rest_framework import viewsets, mixins, status, permissions
from rest_framework.mixins import UpdateModelMixin
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from category.api.serializers import CategorySerializer
from category.models import Category


# list and retrieve enabled category list
from utils.common_methods import EnableDisableViewSet


class CategoryViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    permission_classes = (permissions.AllowAny,)

    serializer_class = CategorySerializer
    queryset = Category.objects.order_by('id').reverse()


# enable and disable category status
# class CategoryEnableDisableViewSet(
#     mixins.UpdateModelMixin,
#     viewsets.GenericViewSet
# ):
#     serializer_class = CategorySerializer
#     queryset = Category.objects.all()
#
#     def partial_update(self, request, *args, **kwargs):
#         kwargs['partial'] = True
#         category_id = kwargs.get('pk')
#         category = Category.objects.get(pk=category_id)
#         if category.status == 1:
#             category.status = 0
#         else:
#             category.status = 1
#         res = category.save(update_fields=["status"])
#         serializer = CategorySerializer(res)
#         return Response(serializer.data, status=status.HTTP_200_OK)


class CategoryEnableDisableViewSet(
    EnableDisableViewSet
):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class ToggleCategoryStatusViewSet(
    mixins.RetrieveModelMixin,
    UpdateModelMixin,
    viewsets.GenericViewSet
):
    permission_classes = (AllowAny,)

    # queryset = Post.all_objects.all()
    # print(queryset)

    def partial_update(self, request, *args, **kwargs):

        kwargs['partial'] = True

        instance = get_object_or_404(Category, pk=kwargs.get('id'))

        if instance.status:
            instance.status = False
        else:
            instance.status = True

        instance.save(update_fields=["status"])
        serializer = CategorySerializer(instance, many=False)

        return Response(status=status.HTTP_200_OK, data=serializer.data)


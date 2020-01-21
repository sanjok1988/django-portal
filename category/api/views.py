from rest_framework import viewsets, mixins

from category.api.serializers import CategorySerializer
from category.models import Category


class CategoryViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    serializer_class = CategorySerializer
    queryset = Category.objects.filter(status=1)


class CategoryDisableViewSet(
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet
):
    serializer_class = CategorySerializer
    queryset = Category.objects.filter(status=1)

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        category_id = kwargs.get('id')
        category = Category.objects.filter(pk=category_id)
        if category:
            category.objects.update(status=0)

        return self.update(request, *args, **kwargs)
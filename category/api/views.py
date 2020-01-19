from rest_framework import viewsets

from category.api.serializers import CategorySerializer
from category.models import Category


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()




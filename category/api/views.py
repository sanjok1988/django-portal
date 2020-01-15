from rest_framework import viewsets

from category.api.serializers import CategorySerializer
from category.models import Category


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


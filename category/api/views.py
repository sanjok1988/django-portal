from rest_framework import viewsets

from posts.api.serializers import PostSerializer
from posts.models import Post
from .serializers import CategorySerializer
from category.models import Category


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get_queryset(self, **kwargs):
        category_id = kwargs['id']
        print(category_id)
        return Post.objects.filter(category=category_id)




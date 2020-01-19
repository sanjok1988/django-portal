from django.db.models import Prefetch
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from category.api.serializers import CategorySerializer
from category.models import Category
from comment.api.serializers import CommentSerializer
from comment.models import Comment
from .serializers import PostSerializer
from ..models import Post


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostByCategoryViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def retrieve(self, request, *args, **kwargs):
        queryset = Post.objects.filter(category=kwargs['pk'])
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)


# fetch all comments and all posts
@api_view(['GET'])
def get_post_comments(request):
    serializer = PostSerializer(Post.objects.all(), many=True)
    return Response(serializer.data)


# fetch singe post details with comments
@api_view(['GET'])
def get_post_detail(request, **kwargs):
    post = get_object_or_404(Post, pk=kwargs.get('id'))
    serializer = PostSerializer(post, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_posts_by_category(request, *args, **kwargs):
    posts = Post.objects.filter(category=kwargs['id'])
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_posts_by_category_slug(request, **kwargs):
    return Response(PostSerializer(Post.objects.filter(category__slug=kwargs.get('slug')), many=True).data)

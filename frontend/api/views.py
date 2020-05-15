from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, generics
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny
from frontend.api.serializers import NewsSerializer, NewsDetailSerializer
from posts.models import Post
from rest_framework.response import Response

from utils.CustomPaginator import HeaderLimitOffsetPagination


class NewsListByCategoryViewSet(
    viewsets.ViewSet
):
    permission_classes = (AllowAny,)
    serializer_class = NewsSerializer

    def list(self, request, slug):
        queryset = Post.objects.all().filter(category__slug=slug).order_by('id').reverse()
        serializer = NewsSerializer(queryset, many=True)
        return Response(serializer.data)

    # def retrieve(self, request, pk=None):
    #     queryset = Post.objects.all()
    #     news = get_object_or_404(queryset, pk=pk)
    #     serializer = NewsSerializer(news)
    #     return Response(serializer.data)


@api_view(['GET'])
def get_post_by_category(request, **kwargs):
    posts = Post.objects.all().filter(category__slug=kwargs.get("cinemas")).order_by('id').reverse()[:4]
    serializer = NewsSerializer(posts, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_popular_news(request):
    posts = Post.objects.all().filter(category__slug="cinemas").order_by('id').reverse()[:4]
    serializer = NewsSerializer(posts, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_post_detail(request, **kwargs):
    post = get_object_or_404(Post, pk=kwargs.get('id'))
    serializer = NewsDetailSerializer(post)
    return Response(serializer.data)


@api_view(['GET'])
def get_post_by_category_with_limit(request, **kwargs):
    query = Post.objects.filter(category__slug=kwargs.get("slug")).order_by('id').reverse()[:kwargs.get('limit')]
    serializer = NewsSerializer(query, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_random_posts(request):
    query = Post.objects.all().order_by('id').reverse()
    serializer = NewsSerializer(query, many=True)
    return Response(serializer.data)


class GetRandomPosts(generics.ListAPIView):
    permission_classes = (AllowAny,)
    queryset = Post.objects.all().order_by('id').reverse()
    serializer_class = NewsSerializer
    pagination_class = HeaderLimitOffsetPagination



from django.contrib.auth.models import User
from django.db.models import Prefetch, Subquery, Max, Count
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, mixins, status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.exceptions import ValidationError
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from category.api.serializers import CategorySerializer
from category.models import Category
from comment.api.serializers import CommentSerializer
from comment.models import Comment
from utils.common_methods import EnableDisableViewSet
from .serializers import PostSerializer, PostListSerializer
from ..models import Post


# fetch list of post
class PostViewSet(
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    queryset = Post.objects.filter(category__status=1)
    serializer_class = PostListSerializer


# fetch post by category
class PostByCategoryViewSet(
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def retrieve(self, request, *args, **kwargs):
        queryset = self.get_queryset().filter(category=kwargs['pk'])
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)


# fetch all post of an author
class PostByAuthorViewSet(
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer

    def list(self, request, *args, **kwargs):
        author = kwargs.get('author')
        try:
            user = User.objects.get(username=author)
        except User.DoesNotExist:
            raise ValidationError({'detail': 'Author not found'})

        queryset = self.get_queryset() \
            .filter(author=user, status=1, category__status=1) \
            .only('title', 'excerpt')  # The only difference between only and values is only also fetches the id.
        # print(str(queryset.query))
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PopularPostViewSet(
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer


# fetch most commented post
class MostCommentedPostViewSet(
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer

    def list(self, request, *args, **kwargs):
        #instance = Comment.objects.values('post_id').order_by('-comment_count').annotate(comment_count=Count('post_id'))[:1]
        data = Comment.objects.values('post_id').order_by('-comment_count').annotate(comment_count=Count('post_id'))

        post_ids = []
        for id in data:
            post_ids.append(id['post_id'])

        posts = self.get_queryset().filter(pk__in=post_ids)
        # max_comment = instance.values('comment_count')
        serializer = self.get_serializer(posts, many=True)
        return Response(serializer.data)


# enable and disable status to 0 and 1
class PostEnableDisableViewSet(
    EnableDisableViewSet
):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer


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

from django.contrib.auth.models import User
from django.db.models import Max, Count, Q
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, mixins, status
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from comment.models import Comment
from utils.common_methods import EnableDisableViewSet
from utils.mixins import UpdateModelMixin
from .serializers import PostSerializer, PostListSerializer, \
    PostDetailSerializer, PostCreateSerializer, ToggleStatusSerializer, PostUpdateSerializer
from posts.models import Post


# fetch list of post
class PostViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet
):
    permission_classes = (AllowAny,)
    # queryset = Post.objects.filter(category__status=1, status=1)
    queryset = Post.objects.all().order_by('id').reverse()
    serializer_class = PostListSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return PostListSerializer
        if self.action == 'create':
            return PostCreateSerializer
        if self.action == 'retrieve':
            return PostDetailSerializer
        if self.action == 'partial_update':
            return PostCreateSerializer

    # using request and response serializer_class different
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = PostCreateSerializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(PostListSerializer(instance).data)


# read detail of post
@permission_classes((IsAuthenticated,))
# @authentication_classes((JSONWebTokenAuthentication,))
class PostDetailViewSet(
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    queryset = Post.objects.filter(status=1, category__status=1)
    serializer_class = PostDetailSerializer


class UnpublishedPostViewSet(
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    queryset = Post.objects.filter(Q(category__status=0) | Q(status=0)).only('title', 'author_id', 'status')
    serializer_class = PostListSerializer


# fetch all soft deleted posts
class PostTrashViewSet(
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    queryset = Post.all_objects.all()
    serializer_class = PostListSerializer


# fetch post by category
class PostByCategoryViewSet(
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    serializer_class = PostSerializer
    queryset = Post.objects.filter(category__status=1, status=1)

    def retrieve(self, request, *args, **kwargs):
        queryset = self.get_queryset().filter(category=kwargs['pk'])
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)


# fetch all post of an author
class PostByAuthorViewSet(
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    queryset = Post.objects.filter(category__status=1, status=1)
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


# most viewed post
class PopularPostViewSet(
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    queryset = Post.objects.filter(category__status=1, status=1).only('title')
    serializer_class = PostListSerializer

    def list(self, request, *args, **kwargs):
        posts = self.get_queryset().order_by().annotate(Max('views_count'))[:5]
        serializer = self.get_serializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# fetch most commented post
class MostCommentedPostViewSet(
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    queryset = Post.objects.filter(category__status=1, status=1)
    serializer_class = PostListSerializer

    def list(self, request, *args, **kwargs):
        data = Comment.objects.values('post_id').order_by('-comment_count').annotate(comment_count=Count('post_id'))[:5]
        posts = self.get_queryset().filter(pk__in=[item['post_id'] for item in data])
        serializer = self.get_serializer(posts, many=True)
        return Response(serializer.data)


# enable and disable status to 0 and 1
class PostEnableDisableViewSet(
    EnableDisableViewSet
):
    permission_classes = (AllowAny,)
    queryset = Post.objects.all()
    serializer_class = ToggleStatusSerializer


class TogglePostStatusViewSet(
    mixins.RetrieveModelMixin,
    UpdateModelMixin,
    viewsets.GenericViewSet
):
    permission_classes = (AllowAny,)

    # queryset = Post.all_objects.all()
    # print(queryset)

    def partial_update(self, request, *args, **kwargs):

        kwargs['partial'] = True

        instance = get_object_or_404(Post, pk=kwargs.get('id'))

        if instance.status:
            instance.status = False
        else:
            instance.status = True

        instance.save(update_fields=["status"])
        serializer = PostListSerializer(instance, many=False)
        print(serializer.data)
        return Response(status=status.HTTP_200_OK, data=serializer.data)


# Enable disable comment on single post
class EnableDisableCommentOnPost(
    UpdateModelMixin,
    viewsets.GenericViewSet
):
    queryset = Post.objects.all()

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        instance = self.queryset.get(pk=kwargs.get('pk'))
        if instance.comment_status == 1:
            instance.comment_status = 0
        else:
            instance.comment_status = 1

        instance.save(update_fields=["comment_status"])

        return Response(status=status.HTTP_200_OK)


# restore soft deleted post
class RestorePostViewSet(
    UpdateModelMixin,
    viewsets.GenericViewSet
):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        post_id = kwargs.get('pk')
        try:
            post = Post.all_objects.get(pk=post_id)
        except Post.DoesNotExist:
            raise ValidationError({'detail': 'Detail not found'})
        post.restore()
        return Response(status=status.HTTP_200_OK)


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

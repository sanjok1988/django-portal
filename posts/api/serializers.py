from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from category.api.serializers import CategorySerializer
from comment.api.serializers import CommentSerializer
from posts.models import Post
from user.api.serializers import AuthorSerializer


class PostSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    author = AuthorSerializer()
    comments = CommentSerializer(many=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'excerpt', 'category', 'author', 'comments']


class PostListSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    author = AuthorSerializer()

    class Meta:
        model = Post
        fields = ['id', 'title', 'excerpt', 'status', 'views_count', 'category', 'author', 'created_at', 'schedule_date']


class PostCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['id', 'title', 'excerpt', 'content', 'status', 'category', 'image', 'author', 'meta_title', 'meta_description']
    #
    # def create(self, validated_data):
    #     print(validated_data)
    #     Post.category.set(validated_data['category'])
    #     post = Post.objects.create(validated_data)


class PostUpdateSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    author = AuthorSerializer()

    class Meta:
        model = Post
        fields = ['id', 'title', 'excerpt', 'status', 'views_count', 'category', 'author', 'meta_title', 'meta_description']


class PostDetailSerializer(serializers.ModelSerializer):
    # category = CategorySerializer()
    # author = AuthorSerializer()
    # comments = CommentSerializer(many=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'sub_title', 'excerpt', 'content', 'file', 'image', 'featured_image',
                  'views_count', 'comment_status', 'category', 'author', 'status', 'meta_title', 'meta_description']


class ToggleStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['status']
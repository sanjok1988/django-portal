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

from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from category.models import Category

from posts.models import Post


class CategoryListSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']


class NewsSerializer(serializers.ModelSerializer):
    category = CategoryListSerializer()

    class Meta:
        model = Post
        fields = ['id', 'title', 'excerpt', 'image', 'category']


class NewsDetailSerializer(serializers.ModelSerializer):
    category = CategoryListSerializer()

    class Meta:
        model = Post
        fields = ['id', 'title', 'sub_title', 'content', 'image', 'category', 'views_count', 'comment_status', 'meta_title', 'meta_description']

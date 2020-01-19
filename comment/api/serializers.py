from rest_framework import serializers
from comment.models import Comment
from user.api.serializers import AuthorSerializer


class CommentSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()

    class Meta:
        model = Comment
        fields = ['id', 'message', 'created_at', 'updated_at', 'author']



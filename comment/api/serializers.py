from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from comment.models import Comment
#from posts.api.serializers import PostSerializer


class CommentSerializer(serializers.ModelSerializer):
    #post = PostSerializer()

    class Meta:
        model = Comment
        fields = ['id', 'message']



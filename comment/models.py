from django.contrib.auth.models import User
from django.db import models

from posts.models import Post


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comment_author")
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE)
    message = models.CharField(max_length=255, blank=False)
    created_at = models.DateTimeField(auto_now=True, auto_created=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False)

    class Meta:
        unique_together = ('post', 'id')

    def __str__(self):
        return '%s' % (self.message,)

    def __unicode__(self):
        return '%d: %s' % (self.id, self.message)

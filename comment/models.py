from django.db import models

from posts.models import Post


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    message = models.CharField(max_length=255, blank=False)
    is_active = models.BooleanField(default=False)

    class Meta:
        unique_together = ('post', 'id')

    def __str__(self):
        return '%s' % (self.message,)

    def __unicode__(self):
        return '%d: %s' % (self.id, self.message)

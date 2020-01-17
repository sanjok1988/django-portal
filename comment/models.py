from django.db import models

# Create your models here.
from posts.models import Post


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    message = models.CharField(max_length=255, blank=False)
    is_active = models.BooleanField(default=False)

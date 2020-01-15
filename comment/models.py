from django.db import models

# Create your models here.
from posts.models import Post


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,)
    message = models.CharField(max_length=255, blank=False)

from django.contrib.auth.models import User
from django.db import models


# Create your models here.
from category.models import Category


class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=100)
    content = models.TextField()
    excerpt = models.TextField(max_length=300)
    file = models.FileField()
    featured_image = models.FileField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    comment_count = models.IntegerField(default=0)
    comment_status = models.IntegerField(default=0)
    status = models.IntegerField(default=0)
    schedule_date = models.DateTimeField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=1, related_name='post_created_by')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, default=1, related_name='post_updated_by')
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django import forms

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.utils.safestring import mark_safe

from category.models import Category
from utils.soft_delete_model import SoftDeletionModel

Status = [
    (1, 'Publish'),
    (0, 'Draft')
]

CommentStatus = [
    (1, 'Allow'),
    (0, 'Disable')
]





class PostManager(models.Manager):
    def get_published(self):
        return Post.objects.filter(status=1, category__status=1)


class Post(SoftDeletionModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1,)
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=100)
    content = RichTextUploadingField()
    excerpt = models.TextField(max_length=300)
    file = models.FileField(null=True, blank=True, upload_to='files/posts/%Y-%m-%d/')
    image = models.ImageField(null=True, blank=True, upload_to='images/posts/%Y-%m-%d/')
    featured_image = models.FileField(null=True, blank=True, upload_to='images/featured/%Y-%m-%d/')
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    comment_count = models.IntegerField(default=0)
    views_count = models.IntegerField(default=0)
    comment_status = models.IntegerField(default=0, choices=CommentStatus)
    status = models.BooleanField(default=False, verbose_name="Publish Status")
    schedule_date = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=1, related_name='post_created_by')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, default=1, related_name='post_updated_by')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # objects = PostManager()
    class Meta:

        pass

    def __str__(self):
        return 'Title:{}, Category: {} '.format(self.title, self.category)

    # def get_published(self):
    #     return Post.objects.filter(status=1, category__status=1)

    @property
    def published_date(self):
        if self.schedule_date is None:
            return self.created_at
        return self.schedule_date

    def featured_image_preview(self):
        url = "https://via.placeholder.com/150/0000FF/808080?Text=Digital.com"
        if self.featured_image:
            url = self.featured_image.url
        return mark_safe('<img src="{url}" width="200" />'.format(url=url))




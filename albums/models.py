from django.contrib.auth.models import User
from django.db import models

Status = [
    (True, 'Publish'),
    (False, 'Draft')
]


# Create your models here.
class Album(models.Model):
    album_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, blank=True)
    cover_photo = models.ImageField(blank=True, null=True, upload_to='images/album/%Y-%m-%d/')
    description = models.TextField(max_length=300, blank=True, null=True)
    status = models.BooleanField(default=False, choices=Status, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=1, related_name='album_created_by')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, default=1, related_name='album_updated_by')
    created_at = models.DateTimeField(auto_now=True, auto_created=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Albums'

    def __str__(self):
        return self.album_name


CommentStatus = [
    (True, 'Allow'),
    (False, 'Disable')
]


class Photo(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, default=1, related_name='photos', null=True, blank=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    photo = models.ImageField(null=True, blank=True, upload_to='images/albums/%Y-%m-%d/')
    caption = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(max_length=300, blank=True, null=True)
    like_count = models.IntegerField(default=0)
    status = models.BooleanField(default=False, verbose_name="Publish Status")
    comment_status = models.BooleanField(default=False, choices=CommentStatus, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=1, related_name='photo_created_by')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, default=1, related_name='photo_updated_by')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Photos'

    def __str__(self):
        return self.title

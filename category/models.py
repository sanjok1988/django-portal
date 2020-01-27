from django.contrib.auth.models import User
from django.db import models


# Create your models here.
from django.template.defaultfilters import slugify


class Category(models.Model):
    name = models.CharField(max_length=80, verbose_name='Category Name')
    slug = models.SlugField(max_length=100)
    status = models.IntegerField(default=1)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=1, related_name='category_created_by')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, default=1, related_name='category_updated_by')
    created_at = models.DateTimeField(auto_now=True, auto_created=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)
        return self

    @property
    def display_status(self):
        if self.status==1:
            return "active"
        else:
            return "deactive"

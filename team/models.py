from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

# Create your models here.
from utils.soft_delete_model import SoftDeletionModel


class Team(SoftDeletionModel):
    member_name = models.CharField(max_length=80)
    position = models.CharField(max_length=40)
    details = RichTextUploadingField(null=True)
    photo = models.ImageField(upload_to='images/team/%Y-%m-%d/', null=True)
    social_links = RichTextUploadingField(null=True, blank=True)
    status = models.BooleanField(default=True)

    class Meta:
        pass

    def __str__(self):
        return 'Name:{}'.format(self.member_name)
from django.db import models

Status = [
    (1, 'enable'),
    (0, 'disable')
]


# Create your models here.
class SiteOptions(models.Model):
    name = models.CharField(max_length=80, unique=True)
    value = models.CharField(max_length=255, blank=True, null=True)
    status = models.BooleanField(default=False, choices=Status)


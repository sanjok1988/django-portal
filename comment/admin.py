from django.contrib import admin

# Register your models here.
from comment.models import Comment


@admin.register(Comment)
class AdminComment(admin.ModelAdmin):
    list_display = ['post', 'message']
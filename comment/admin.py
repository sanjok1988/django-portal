from django.contrib import admin

# Register your models here.
from comment.models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'message', 'is_active']
    actions = ['approve_comments']

    # def approve_comments(self, request, queryset):
    #     queryset.update(is_active=True)

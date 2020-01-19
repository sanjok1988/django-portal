from django.contrib import admin

# Register your models here.
from comment.models import Comment


@admin.register(Comment)
class AdminComment(admin.ModelAdmin):
    list_display = ['id', 'message']
    actions = ['approve_comments']

    # def approve_comments(self, request, queryset):
    #     queryset.update(is_active=True)

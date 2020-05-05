from django.contrib import admin

# Register your models here.
from comment.models import Comment
from team.models import Team


@admin.register(Team)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'member_name', 'status']

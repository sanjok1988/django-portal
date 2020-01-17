from django.contrib import admin


# Register your models here.
#
# @admin.register(Post)
# @data_generator_register
from posts.models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category', 'status']
    list_filter = ('category', 'status')
    search_fields = ('title',)


admin.site.register(Post, PostAdmin)

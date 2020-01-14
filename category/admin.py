from django.contrib import admin

# Register your models here.
from category.models import Category
from posts.models import Post


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post)

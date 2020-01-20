from data_seeder.admin import data_generator_register
from django.contrib import admin

# Register your models here.
from category.models import Category
from posts.models import Post


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ['id', 'name', 'status']
    list_filter = ['status']

    fieldsets = [
            ( None, { 'fields' : ['name', 'slug']}),
            ('Additional Info', { 'fields' : ['status',]}),
        ]

admin.site.register(Category, CategoryAdmin)




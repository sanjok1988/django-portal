from django import forms
from django.contrib import admin
from django.contrib.admin import SimpleListFilter
from category.models import Category
from posts.models import Post
from utils.mixins import ExportCsvMixin


class PopularPostFilter(SimpleListFilter):
    title = 'Popular Posts'  # _('popular Post')
    parameter_name = 'popular_post'

    def lookups(self, request, model_admin):
        return

    def queryset(self, request, queryset):
        pass


class CategoryChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return "{}".format(obj.name)


class PostAdmin(admin.ModelAdmin, ExportCsvMixin):

    fields = ('schedule_date', 'category', 'title', 'sub_title', 'content', 'excerpt', 'author', 'featured_image',
              'featured_image_preview',
              'image', 'file', 'comment_status', 'status',)
    list_display = ['id', 'title', 'category', 'author', 'is_published', ]
    list_filter = (PopularPostFilter, 'category', 'status',)
    search_fields = ('title',)
    list_display_links = ('title',)
    list_select_related = ('author', 'category')
    raw_id_fields = ("category",)
    list_per_page = 20
    date_hierarchy = 'created_at'
    readonly_fields = ["featured_image_preview", ]

    def is_published(self, obj):
        return obj.status

    is_published.boolean = True

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return CategoryChoiceField(queryset=Category.objects.all())
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Post, PostAdmin)

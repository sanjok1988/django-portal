from django.contrib import admin

# Register your models here.
#
# @admin.register(Post)
# @data_generator_register
from django.contrib.admin import SimpleListFilter
from pylint.checkers.typecheck import _

from posts.models import Post
from utils.mixins import ExportCsvMixin


class PopularPostFilter(SimpleListFilter):
    title = 'Popular Posts'  # _('popular Post')
    parameter_name = 'popular_post'

    def lookups(self, request, model_admin):
        return

    def queryset(self, request, queryset):
        pass


class PostAdmin(admin.ModelAdmin, ExportCsvMixin):
    list_display = ['id', 'title', 'category', 'author', 'is_published',]
    list_filter = (PopularPostFilter, 'category', 'status',)
    search_fields = ('title',)
    list_display_links = ('title',)
    list_select_related = ('author', 'category')
    raw_id_fields = ("category",)
    list_per_page = 20
    date_hierarchy = 'created_at'
    readonly_fields = ["featured_image_preview",]



    def is_published(self, obj):
        return obj.status

    is_published.boolean = True

    # def featured_image_preview(self, obj):
    #     print(obj.featured_image.url)
    #     print(obj.featured_image.width)
    #     return mark_safe('<img src="{url}" width="150" height="150" />'.format(
    #         url=obj.featured_image.url,
    #
    #     ))


admin.site.register(Post, PostAdmin)

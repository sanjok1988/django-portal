from django.contrib import admin


# Register your models here.
#
# @admin.register(Post)
# @data_generator_register
from django.contrib.admin import SimpleListFilter
from pylint.checkers.typecheck import _

from posts.models import Post


class PopularPostFilter(SimpleListFilter):
    title = 'Popular Posts' # _('popular Post')
    parameter_name = 'popular_post'

    def lookups(self, request, model_admin):
        return

    def queryset(self, request, queryset):
        pass


class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category', 'is_published',]
    list_filter = (PopularPostFilter, 'category', 'status', )
    search_fields = ('title',)
    list_display_links = ('title',)
    list_select_related = ('author', 'category')
    raw_id_fields = ("category",)


    def is_published(self, obj):
        return obj.status

    is_published.boolean = True

admin.site.register(Post, PostAdmin)

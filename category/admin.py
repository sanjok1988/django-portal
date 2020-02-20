from django.contrib import admin

# Register your models here.
from django.http import HttpResponseRedirect
from django.urls import path
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from category.models import Category
from utils.mixins import ExportCsvMixin


class CategoryResource(resources.ModelResource):
    class Meta:
        model = Category
        fields = ('id', 'name', 'post__author',)
        export_order = ('id', 'name', 'post__author')


class CategoryAdmin(ImportExportModelAdmin, ExportCsvMixin ):
    #change_list_template = "admin/category/category/category_change_list.html"

    prepopulated_fields = {"slug": ("name",)}
    list_display = ['name', 'post_count', 'display_status']
    list_filter = ['status']
    actions = ["export_as_csv", "unpublish"]
    list_display_links = ['name', ]
    ordering = ('name',)

    resource_class = CategoryResource


    fieldsets = [
        (None, {'fields': ['name', 'slug']}),
        ('Additional Info', {'fields': ['status', ]}),
    ]

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('activate/', self.set_status),
            path('deactivate/', self.set_deactivate),
        ]
        return my_urls + urls

    # additional action in admin
    def unpublish(self, request, queryset):
        for obj in queryset:
            obj.status = 0
            obj.save()
        return

    def set_status(self, request):
        self.model.objects.all().update(status=1)
        self.message_user(request, "All categories are now activated")
        return HttpResponseRedirect("../")

    def set_deactivate(self, request):
        self.model.objects.all().update(status=0)
        self.message_user(request, "All categories are now deactivated")
        return HttpResponseRedirect("../")

    # remove delete selected action from admin panel
    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    def post_count(self, obj):
        return obj.post_set.count()


admin.site.register(Category, CategoryAdmin)

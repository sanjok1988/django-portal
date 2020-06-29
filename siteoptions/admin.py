from django.contrib import admin

# Register your models here.
from siteoptions.models import SiteOptions


class SiteOptionsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'value', 'status']
    list_display_links = ['name', ]


admin.site.register(SiteOptions, SiteOptionsAdmin)

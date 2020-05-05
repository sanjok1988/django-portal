from django.contrib import admin

# Register your models here.
from albums.models import Album, Photo


class PhotoAdminInline(admin.TabularInline):
    model = Photo
    readonly_fields = ['like_count', 'created_by', 'updated_by']
    extra = 3


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    readonly_fields = ['created_by', 'updated_by']
    inlines = [PhotoAdminInline, ]
    list_display = ['id', 'album_name', 'status']


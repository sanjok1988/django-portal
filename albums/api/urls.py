from django.urls import path
from rest_framework import routers

from albums.api.views import AlbumViewSet, PhotoViewSet, UploadToAlbumViewSet

router = routers.DefaultRouter()
router.register(r'album', viewset=AlbumViewSet)
router.register(r'photo', viewset=PhotoViewSet)

urlpatterns = [
    path('album/<int:id>/photos', UploadToAlbumViewSet.as_view({'post': 'create', 'get':'list'}))
]
urlpatterns += router.urls

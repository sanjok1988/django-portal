from rest_framework import routers

from albums.api.views import AlbumViewSet, PhotoViewSet

router = routers.DefaultRouter()
router.register(r'album', viewset=AlbumViewSet)
router.register(r'photo', viewset=PhotoViewSet)

urlpatterns = []
urlpatterns += router.urls
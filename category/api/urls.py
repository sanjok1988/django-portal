from rest_framework import routers

from category.api.views import CategoryViewSet, CategoryEnableDisableViewSet

router = routers.SimpleRouter()
router.register(r'category', viewset=CategoryViewSet)
router.register(r'enable-disable', viewset=CategoryEnableDisableViewSet)
urlpatterns = [

]
urlpatterns += router.urls

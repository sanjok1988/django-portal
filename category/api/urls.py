from rest_framework import routers

from category.api.views import CategoryViewSet, CategoryDisableViewSet

router = routers.SimpleRouter()
router.register(r'category', viewset=CategoryViewSet)
router.register(r'disable', viewset=CategoryDisableViewSet)
urlpatterns = [

]
urlpatterns += router.urls

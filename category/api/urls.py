from rest_framework import routers

from category.api.views import CategoryViewSet

router = routers.SimpleRouter()
router.register(r'category', viewset=CategoryViewSet)

urlpatterns = [

]
urlpatterns += router.urls

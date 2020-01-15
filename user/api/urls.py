from rest_framework import routers

from user.api import views
from user.api.views import UserViewSet, GroupViewSet

router = routers.SimpleRouter()
router.register(r'user', viewset=UserViewSet)
router.register(r'group', viewset=GroupViewSet)
urlpatterns = [

]
urlpatterns += router.urls
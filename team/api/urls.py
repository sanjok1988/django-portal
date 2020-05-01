from rest_framework import routers

from team.api.views import TeamViewSet

router = routers.DefaultRouter()
router.register(r'team', viewset=TeamViewSet)

urlpatterns = []
urlpatterns += router.urls
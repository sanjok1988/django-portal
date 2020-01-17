from django.urls import path
from rest_framework import routers

from user.api import views
from user.api.views import UserViewSet, GroupViewSet, get_users, UserList

router = routers.SimpleRouter()
router.register(r'user', viewset=UserViewSet)
router.register(r'group', viewset=GroupViewSet)
urlpatterns = [
    path('users/', get_users ),
    path('usrs/', UserList.as_view())
]
urlpatterns += router.urls
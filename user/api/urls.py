from django.conf.urls import url
from django.urls import path
from rest_framework import routers

from user.api import views
from user.api.views import UserViewSet, GroupViewSet, get_users, UserList, get_permissions, Permissions, LoginView, RegisterUserView
from rest_framework_simplejwt import views as jwt_views

router = routers.SimpleRouter()
router.register(r'user', viewset=UserViewSet)
# router.register(r'group', viewset=GroupViewSet)
# router.register(r'per', viewset=Permissions)
urlpatterns = [


    # path("login/", LoginView.as_view(), name="login"),
    # path("drf/login/", views.obtain_auth_token, name="drf-login"),
    # path('users/', get_users ),
    # path('usrs/', UserList.as_view()),
    # path('permissions/', get_permissions),
    # path('permissions/<int:user_id>/', views.Permissions.as_view({"get": "get_user_permission"})),
    # path('perms/', Permissions.as_view({'get': 'list'}))
]
urlpatterns += router.urls
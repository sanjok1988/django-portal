from django.urls import path
from rest_framework import routers

from category.api.views import CategoryViewSet, CategoryEnableDisableViewSet, ToggleCategoryStatusViewSet

router = routers.SimpleRouter()
router.register(r'category', viewset=CategoryViewSet)
router.register(r'enable-disable', viewset=CategoryEnableDisableViewSet)
urlpatterns = [
    path('category/toggle-status/<int:id>', ToggleCategoryStatusViewSet.as_view({'patch': 'partial_update'}))
]
urlpatterns += router.urls

from django.urls import path
from rest_framework import routers

from .views import PostByCategoryViewSet, PostViewSet, get_posts_by_category, get_posts_by_category_slug, \
    get_post_comments, get_post_detail

router = routers.DefaultRouter()
router.register(r'post', viewset=PostViewSet)
# router.register(r'category', viewset=PostByCategoryViewSet)


urlpatterns = [
    path('cat/<int:id>', get_posts_by_category, name='po_view'),
    path('cat/<slug:slug>', get_posts_by_category_slug, name='slug'),
    path('comments', get_post_comments, name='comments'),
    path('comment/post/<int:id>', get_post_detail)
]
urlpatterns += router.urls

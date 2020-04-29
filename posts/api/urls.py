from django.urls import path
from rest_framework import routers

from .views import PostByCategoryViewSet, PostViewSet, get_posts_by_category, get_posts_by_category_slug, \
    get_post_comments, get_post_detail, PostEnableDisableViewSet, PostByAuthorViewSet, MostCommentedPostViewSet, \
    EnableDisableCommentOnPost, PostTrashViewSet, PopularPostViewSet, PostDetailViewSet, RestorePostViewSet, \
    UnpublishedPostViewSet, TogglePostStatusViewSet

router = routers.DefaultRouter()
router.register(r'post', viewset=PostViewSet)
router.register(r'category', viewset=PostByCategoryViewSet)
router.register(r'detail', viewset=PostDetailViewSet)
router.register(r'unpublished', viewset=UnpublishedPostViewSet)

# router.register(r'post/toggle-status', viewset=PostEnableDisableViewSet)
router.register(r'enable-disable/comment', viewset=EnableDisableCommentOnPost)

router.register(r'most-discussed', viewset=MostCommentedPostViewSet)
router.register(r'most-popular', viewset=PopularPostViewSet)

router.register(r'trash', viewset=PostTrashViewSet)
router.register(r'restore', viewset=RestorePostViewSet)


urlpatterns = [
    path('cat/<int:id>', get_posts_by_category, name='po_view'),
    path('cat/<slug:slug>', get_posts_by_category_slug, name='slug'),
    path('comments', get_post_comments, name='comments'),
    path('comment/post/<int:id>', get_post_detail),
    path('author/<str:author>', PostByAuthorViewSet.as_view({'get': 'list'})),
    path('post/toggle-status/<int:id>', TogglePostStatusViewSet.as_view({'patch': 'partial_update'}))
]
urlpatterns += router.urls

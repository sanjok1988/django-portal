from django.urls import path
from rest_framework import routers

from frontend.api import views
from frontend.api.views import NewsListByCategoryViewSet, GetRandomPosts

router = routers.DefaultRouter()
# router.register(r'posts', viewset=PostsViewSet)
# router.register(r'photo', viewset=PhotoViewSet)

urlpatterns = [
    path('news/list/<slug>/', NewsListByCategoryViewSet.as_view()),
    path('news/popular/', views.get_popular_news, name="popular_news"),
    path('news/post/<int:id>', views.get_post_detail, name="post_detail"),
    path('news/category/<slug>', views.get_post_by_category, name="post_by_category"),
    path('news/category/<slug>/limit/<int:limit>', views.get_post_by_category_with_limit, name="post_by_category_with_limit"),
    # path('news/random/', views.get_random_posts, name='random_posts')
    path('news/random/', GetRandomPosts.as_view())
]
urlpatterns += router.urls

from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    CategoryViewSet, CommentViewSet, GenreViewSet, ReviewViewSet,
    TitleViewSet,
)

router_1 = DefaultRouter()
router_1.register(r'genres', GenreViewSet, basename='genres')
router_1.register(r'categories', CategoryViewSet, basename='categories')
router_1.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet,
    basename='reviews'
)
router_1.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)
router_1.register(r'titles', TitleViewSet, basename='titles')

urlpatterns = [
    path('v1/users/', include('users.urls')),
    path('v1/auth/', include('users.urls')),
    path('v1/', include(router_1.urls)),
]

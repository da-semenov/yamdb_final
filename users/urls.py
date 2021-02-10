from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CustomUserViewSet, get_confirmation_code, get_jwt_token

router_1 = DefaultRouter()
router_1.register(r'', CustomUserViewSet, basename='users')

urlpatterns = [
    path('email/', get_confirmation_code, name='token_obtain_pair'),
    path('token/', get_jwt_token, name='token'),
    path('', include(router_1.urls)),
]

from django.urls import include, path

# Routers provide an easy way of automatically determining the URL conf.
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import UserSerializerViewSet

# Router for apps
router = routers.DefaultRouter()

router.register("users", UserSerializerViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]

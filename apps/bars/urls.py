from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import BarOwnerView, BarViewSet

router = DefaultRouter()
router.register("bars", BarViewSet)

urlpatterns = [
    path("bars/owner/", BarOwnerView.as_view()),
    path("", include(router.urls)),
]

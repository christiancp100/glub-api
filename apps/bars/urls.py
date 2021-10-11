from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BarViewSet, BarOwnerView

router = DefaultRouter()
router.register("bars", BarViewSet)

urlpatterns = [
    path('bars/owner/', BarOwnerView.as_view()),
    path('', include(router.urls))
]

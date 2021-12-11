from django.urls import path
from rest_framework.routers import DefaultRouter
from apps.suggestions import views

router = DefaultRouter()

router.register(r'suggest', views.SuggestionViewSet, basename='Suggestion')

urlpatterns = router.urls


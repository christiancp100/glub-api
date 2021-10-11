from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.events.views import EventViewSet
router = DefaultRouter()

router.register("events", EventViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/', include('apps.accounts.urls')),
    path('api/', include('apps.bars.urls')),
    path('api/registry/', include('apps.registry.urls')),
]

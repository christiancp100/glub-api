from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.events.views import EventViewSet
from config import settings

router = DefaultRouter()

router.register("events", EventViewSet)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("api/", include("apps.accounts.urls")),
    path("api/", include("apps.bars.urls")),
    path("api/", include("apps.events.urls")),
    path("api/", include("apps.tickets.urls")),
    path("api/registry/", include("apps.registry.urls")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

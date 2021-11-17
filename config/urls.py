from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.conf.urls.static import static
from apps.events.views import EventViewSet
from config import settings
router = DefaultRouter()

router.register("events", EventViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/', include('apps.accounts.urls')),
    path('api/', include('apps.bars.urls')),
    path('api/', include('apps.events.urls')),
    path('api/', include('apps.tickets.urls')),
    path('api/registry/', include('apps.registry.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


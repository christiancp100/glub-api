from django.urls import path, include
from .views import UserSerializerViewSet
# Routers provide an easy way of automatically determining the URL conf.
from rest_framework import routers

# Router for apps
router = routers.DefaultRouter()

router.register('profile', UserSerializerViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
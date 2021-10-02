from django.urls import path, include
from .views import create_partial_user


urlpatterns = [
    path('registry/create-user/', create_partial_user, name='create-partial-user'),
]
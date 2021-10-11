from django.urls import path
from .views import CreatePartialUserView, RegistryView

urlpatterns = [
    path('', RegistryView.as_view(), name="registry-view"),
    path('create-user/', CreatePartialUserView.as_view())
]

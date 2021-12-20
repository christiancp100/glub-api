from django.urls import path

from .views import CapacityView, CreatePartialUserView, RegistryView

urlpatterns = [
    path("access/", RegistryView.as_view(), name="registry-view"),
    path("decrease-capacity/", CapacityView.as_view({"post": "decrease_capacity"})),
    path("increase-capacity/", CapacityView.as_view({"post": "increase_capacity"})),
    path("create-user/", CreatePartialUserView.as_view()),
]

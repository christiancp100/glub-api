from django.urls import path
from .views import CreatePartialUserView


urlpatterns = [
    path('registry/create-user/', CreatePartialUserView.as_view())
]
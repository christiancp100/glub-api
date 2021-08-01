from django.shortcuts import render
from rest_framework import viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication
from  rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.exceptions import NotAuthenticated
from .permissions import UpdateOwn, IsAdmin
from .serializers import UserSerializer
from .models import User


# Create your views here.

class UserSerializerViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    authentication_classes = (JWTAuthentication, BasicAuthentication, SessionAuthentication)
    permission_classes = [UpdateOwn | IsAdmin]

    def get_queryset(self):
        if self.request.user.is_superuser:
            return User.objects.all()
        if self.request.user.is_authenticated:
            return User.objects.filter(email=self.request.user)
        raise NotAuthenticated()



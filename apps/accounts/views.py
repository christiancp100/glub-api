from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import User, UserProfile
from .permissions import IsAdmin, UpdateOwn
from .serializers import UserSerializer


class UserSerializerViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    authentication_classes = (
        JWTAuthentication,
        BasicAuthentication,
        SessionAuthentication,
    )
    permission_classes = [UpdateOwn | IsAdmin]

    def get_serializer_class(self):
        return UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        if self.request.user.is_superuser:
            users = User.objects.all()
            serializer = self.get_serializer(users, many=True)
            return Response(serializer.data)
        raise PermissionDenied()

    def retrieve(self, request, *args, **kwargs):
        if self.request.user.is_superuser or self.request.user == self.get_object():
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        raise PermissionDenied()

    def update(self, request, *args, **kwargs):
        kwargs["partial"] = True
        profile_data = request.data.pop("profile")
        UserProfile.objects.filter(user_id=self.get_object().id).update(**profile_data)
        return super().update(request, *args, **kwargs)

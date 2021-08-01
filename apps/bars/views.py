from django.shortcuts import get_object_or_404
from rest_framework.response import Response

from .models import Bar
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.exceptions import NotFound
from rest_framework import viewsets, status
from apps.bars.serializers import BarSerializer
from ..accounts.models import User
from ..accounts.permissions import IsOwnerOrReadOnly


class BarViewSet(viewsets.ModelViewSet):
    authentication_classes = (BasicAuthentication, SessionAuthentication, JWTAuthentication)
    queryset = Bar.objects.all()
    serializer_class = BarSerializer
    permission_classes = (IsOwnerOrReadOnly,)

    def get_queryset(self):
        return self.queryset.all().order_by('-name')

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if self.request.user.is_superuser:
            owner = get_object_or_404(User, id=request.data.get('owner'))
        else:
            owner = self.request.user
        serializer.is_valid(raise_exception=True)
        bar = Bar.objects.create(owner=owner, **serializer.data)
        return Response(BarSerializer(bar).data, status=status.HTTP_201_CREATED)

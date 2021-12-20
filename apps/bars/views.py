from django.db import IntegrityError
from django.shortcuts import get_object_or_404
from rest_framework import generics, status, viewsets
from rest_framework.exceptions import NotAcceptable
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response

from apps.bars.serializers import BarDetailSerializer, BarImageSerializer, BarSerializer
from config.settings import AUTH_METHODS

from ..accounts.models import User
from ..accounts.permissions import IsOwner, IsOwnerOrReadOnly
from .models import Bar


class BarViewSet(viewsets.ModelViewSet):
    authentication_classes = AUTH_METHODS
    queryset = Bar.objects.all()
    serializer_class = BarSerializer
    permission_classes = (IsOwnerOrReadOnly,)
    parser_classes = (MultiPartParser, FormParser)

    def get_serializer_class(self):
        if self.action == "retrieve" or self.action == "create":
            return BarDetailSerializer
        return BarSerializer

    def get_queryset(self):
        return self.queryset.all().order_by("-name")

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        if self.request.user.is_superuser:
            owner = get_object_or_404(User, id=request.data.get("ownerId"))
        else:
            owner = self.request.user

        try:
            bar = Bar.objects.create(owner=owner, **serializer.validated_data)
            try:
                images = request.FILES.getlist("images")
                for image in images:
                    data = {
                        "bar": bar.id,
                        "image": image,
                    }
                    bar_image = BarImageSerializer(data=data)
                    if bar_image.is_valid(raise_exception=True):
                        bar_image.save()
            except IntegrityError:
                raise NotAcceptable("No se han podido añadir las images del bar")
        except IntegrityError:
            raise NotAcceptable("Ya tienes un bar con ese nombre")

        return Response(self.get_serializer(bar).data, status=status.HTTP_201_CREATED)


class BarOwnerView(generics.ListAPIView):
    serializer_class = BarSerializer
    permission_classes = [IsOwner]

    def get_queryset(self):
        return Bar.objects.filter(owner_id=self.request.user.id)

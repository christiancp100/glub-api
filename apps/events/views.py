from rest_framework import viewsets, status
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from apps.events.models import Event
from apps.bars.models import Bar
from apps.events.serializers import EventSerializer
from .permissions import IsOwnerOrReadOnly


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = (IsOwnerOrReadOnly,)

    def get_queryset(self):
        if self.request.user.is_superuser:
            return self.queryset.all().order_by('start_date')
        return self.queryset.filter(is_active=True).order_by('start_date')

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        bar = get_object_or_404(Bar, id=request.data.get('bar'))
        event = Event.objects.create(bar=bar, created_by=self.request.user, **serializer.validated_data)
        return Response(EventSerializer(event).data, status=status.HTTP_201_CREATED)

    def destroy(self, request, *args, **kwargs):
        print("F: ", self.get_object())
        event = self.get_object()
        event.is_active = False
        event.save()
        return Response(EventSerializer(event).data, status=status.HTTP_202_ACCEPTED)
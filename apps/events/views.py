from rest_framework import viewsets
from apps.events.models import Event
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



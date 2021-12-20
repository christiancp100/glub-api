from rest_framework import serializers

from apps.accounts.serializers import UserSerializer
from apps.events.serializers import EventSerializer

from .models import Ticket


class TicketSerializer(serializers.ModelSerializer):
    event = EventSerializer(read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Ticket
        fields = ("event", "user", "is_paid", "is_ticked")

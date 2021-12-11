from rest_framework import serializers
from .models import Suggestion
from apps.events.serializers import EventSerializer
from apps.accounts.serializers import UserSerializer


class SuggestionSerializer(serializers.ModelSerializer):
    event = EventSerializer()
    user = UserSerializer()

    class Meta:
        model = Suggestion
        fields = '__all__'
        read_only_fields = ('id',)

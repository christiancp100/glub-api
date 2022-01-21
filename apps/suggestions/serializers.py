from rest_framework import serializers
from .models import Suggestion
from apps.events.serializers import EventSerializer
from apps.accounts.serializers import UserSerializer
from apps.events.models import Event


class SuggestionSerializer(serializers.ModelSerializer):
    event = EventSerializer(read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Suggestion
        fields = '__all__'


class SimpleSuggestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suggestion
        fields = ('song_title',)

"""
class IdEvent(serializers.ModelSerializer):
    class Meta:
        model = Suggestion
        fields = ('id',)



class NameOfEvent(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields= ('name',)
        """


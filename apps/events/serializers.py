from datetime import datetime
from django.utils import timezone
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from apps.events.models import Event
from apps.bars.serializers import BarSerializer


class EventSerializer(serializers.ModelSerializer):
    bar = BarSerializer(read_only=True)

    def validate(self, attrs):
        if attrs.get("start_date") < timezone.now():
            raise ValidationError("La fecha de inicio es anterior a la fecha actual")
        if attrs.get("finish_date") < timezone.now():
            raise ValidationError("La fecha de fin es anterior a la fecha actual")
        if attrs.get("start_date") >= attrs.get("finish_date"):
            raise ValidationError("La fecha de inicio debe ser anterior a la de fin.")
        return attrs

    class Meta:
        model = Event
        fields = ('name', 'description', 'start_date', 'finish_date', 'capacity', 'bar')
        read_only_fields = ('id',)

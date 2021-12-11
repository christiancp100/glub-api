from django.db import models
from apps.accounts.models import User
from apps.events.models import Event


class Suggestion(models.Model):
    class Meta:
        unique_together = ('user', 'event')

    song_title = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, blank=False)

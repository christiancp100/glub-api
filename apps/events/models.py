from django.db import models
from apps.accounts.models import User

# Create your models here.
from apps.bars.models import Bar


class EventManager(models.Manager):

    def get_bar_events(self, bar):
        self.filter(bar=bar)

    def get_events_range(self, from_date, to_date):
        self.filter(start_date__lte=from_date, finish_date__gte=to_date)


class Event(models.Model):
    name = models.CharField(max_length=120, blank=False)
    description = models.CharField(max_length=500, blank=True)
    start_date = models.DateTimeField(blank=False)
    finish_date = models.DateTimeField(blank=False)
    capacity = models.IntegerField(blank=False)
    is_active = models.BooleanField(default=True)
    # TODO Add images
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)
    bar = models.ForeignKey(Bar, on_delete=models.PROTECT, blank=False)

    objects = EventManager()

    def delete(self, using=None, keep_parents=False):
        self.is_active = False
        self.save()

    def __str__(self):
        return self.name


class EventImage(models.Model):
    pass

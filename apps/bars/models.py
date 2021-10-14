from django.db import models
from apps.accounts.models import User


class BarManager(models.Manager):

    def get_bars_by_owner(self, owner):
        return self.filter(owner=owner)

    def is_owned_by_owner(self, bar_id, owner_id):
        bar = self.get(id=bar_id)
        if bar:
            return bar.owner.id == owner_id
        return False


class Bar(models.Model):
    class Meta:
        unique_together = ('name', 'owner')

    # TODO Add logo and images
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    name = models.CharField(max_length=60, default="Anonymous Bar", blank=False, null=False)
    address = models.CharField(max_length=100, blank=False, null=False)
    capacity = models.IntegerField(default=100, blank=False, null=False)
    current_capacity = models.IntegerField(default=0, blank=False, null=False)
    is_active = models.BooleanField(default=True)

    objects = BarManager()

    def increase_capacity(self):
        if self.current_capacity <= self.capacity:
            self.current_capacity += 1
            self.save()

    def decrease_capacity(self):
        if self.current_capacity > 0:
            self.current_capacity -= 1
            self.save()

    def __str__(self):
        return self.name

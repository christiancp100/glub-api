from django.db import models
from apps.accounts.models import User


class Bar(models.Model):
    class Meta:
        unique_together = ('name', 'owner')

    # TODO Add logo and images
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=60, default="Anonymous Bar", blank=False, null=False)
    address = models.CharField(max_length=100, blank=False, null=False)
    capacity = models.IntegerField(default=100, blank=False, null=False)
    # is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name


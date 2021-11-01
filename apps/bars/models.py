from django.db import models
from apps.accounts.models import User
from config import settings


class BarManager(models.Manager):

    def get_bars_by_owner(self, owner):
        return self.filter(owner=owner)

    def is_owned_by_owner(self, bar_id, owner_id):
        bar = self.get(id=bar_id)
        if bar:
            return bar.owner.id == owner_id
        return False


def upload_to(instance, filename):
    return 'baricons/{filename}'.format(filename=filename)


def default_image():
    return settings.MEDIA_ROOT + 'baricons/default_image.png'


class Bar(models.Model):
    class Meta:
        unique_together = ('name', 'owner')

    # TODO Add logo and images
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    name = models.CharField(max_length=60, default="Anonymous Bar", blank=False, null=False)
    address = models.CharField(max_length=100, blank=False, null=False)
    capacity = models.IntegerField(default=100, blank=False, null=False)
    is_active = models.BooleanField(default=True)
    image_file = models.ImageField(upload_to=upload_to, default=default_image())

    objects = BarManager()

    def __str__(self):
        return self.name


class BarIcon(models.Model):
    image_name = models.CharField(max_length=32)
    image_file = models.ImageField(upload_to=upload_to)

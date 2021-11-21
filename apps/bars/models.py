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


def upload_to(instance, filename):
    return 'bars/{bar_name}/logo/{filename}'.format(bar_name=instance.name, filename=filename)


class Bar(models.Model):
    class Meta:
        unique_together = ('name', 'owner')

    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=60, default="Anonymous Bar", blank=False, null=False)
    address = models.CharField(max_length=100, blank=False, null=False)
    capacity = models.IntegerField(default=100, blank=False, null=False)
    current_capacity = models.IntegerField(default=0, blank=False, null=False)
    is_active = models.BooleanField(default=True)
    logo = models.ImageField(upload_to=upload_to, blank=True, null=True)

    objects = BarManager()

    def __str__(self):
        return self.name


def upload_to_bar_images_folder(instance, filename):
    return 'bars/{bar_name}/images/{filename}'.format(bar_name=instance.bar, filename=filename)


class BarImages(models.Model):
    bar = models.ForeignKey(Bar, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to=upload_to_bar_images_folder, blank=True, null=True)
    description = models.CharField(max_length=100, blank=False, null=False)

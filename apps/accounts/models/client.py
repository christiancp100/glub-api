from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

from .user import User

"""
class ClientManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.CLIENT)


class Client(User):
    base_type = User.Types.CLIENT
    objects = ClientManager()

    class Meta:
        proxy = True

    @property
    def more(self):
        return self.clientinfo

    def save(self, *args, **kwargs):
        if not self.id:
            self.type = User.Types.CLIENT
        return super().save(*args, **kwargs)


class ClientInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthday = models.DateField()
"""
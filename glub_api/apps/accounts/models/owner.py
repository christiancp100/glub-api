from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

from .user import User


class OwnerManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.OWNER)


class Owner(User):
    base_type = User.Types.OWNER
    objects = OwnerManager()

    class Meta:
        proxy = True

    @property
    def more(self):
        return self.ownerinfo

    def save(self, *args, **kwargs):
        if not self.id:
            self.type = User.Types.OWNER
        return super().save(*args, **kwargs)


class OwnerInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nif = models.CharField(max_length=8)

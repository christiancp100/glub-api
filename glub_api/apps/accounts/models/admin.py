from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

from .user import User


class AdminManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.ADMIN)


class Admin(User):
    base_type = User.Types.OWNER
    objects = AdminManager()

    class Meta:
        proxy = True

    @property
    def more(self):
        return self.admininfo

    def save(self, *args, **kwargs):
        if not self.id:
            self.type = User.Types.ADMIN
        return super().save(*args, **kwargs)


class AdminInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=(('CTO', 'CTO'), ('CEO', 'CEO'), ('COO', 'COO'), ('Other', 'Other')))

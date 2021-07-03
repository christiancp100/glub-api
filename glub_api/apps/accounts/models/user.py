from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Types(models.TextChoices):
        CLIENT = "CLIENT", "Client"
        OWNER = "OWNER", "Owner"
        ADMIN = "ADMIN", "Admin"

    base_type = Types.CLIENT

    type = models.CharField(max_length=40, choices=Types.choices, default=base_type)
    username = models.CharField(blank=False, null=False, unique=True, max_length=50)

    def more(self):
        pass

    def save(self, *args, **kwargs):
        if not self.id:
            self.type = self.base_type
        return super().save(*args, **kwargs)

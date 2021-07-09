from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models

"""
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
"""


class UserManager(BaseUserManager):
    def create_user(self, email, password, name, **kwargs):
        if not email or not password:
            raise ValueError("El email y la contraseña son obligatorios")
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_owner(self, email, password, name, **kwargs):
        user = self.create_user(email, password, name, **kwargs)
        user.is_staff = True
        user.is_owner = True
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password, name, **kwargs):
        user = self.create_owner(email, password, name, **kwargs)
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_owner = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name

    def __str__(self):
        return self.email

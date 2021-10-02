from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from config import settings


class UserManager(BaseUserManager):
    def create(self, **validated_data):
        email = self.normalize_email(validated_data.pop("email", None))
        password = validated_data.pop("password", None)
        user = self.model(email=email, **validated_data)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, **validated_data):
        profile_data = validated_data.pop('profile')
        user = self.create(**validated_data)
        UserProfile.objects.create(user=user, **profile_data)
        return user

    def create_owner(self, **validated_data):
        user = self.create(**validated_data)
        user.is_staff = True
        user.is_owner = True
        user.save(using=self._db)
        return user

    def create_superuser(self, **validated_data):
        user = self.create_owner(**validated_data)
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_owner = models.BooleanField(default=False)
    is_completed = models.BooleanField(default=True)

    def get_profile(self):
        return UserProfile.objects.get(user_id=self.id)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def get_full_name(self):
        return self.first_name + " " + self.last_name

    def get_short_name(self):
        return self.first_name

    def __str__(self):
        return self.email


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    phone = models.CharField(max_length=9)
    address = models.CharField(max_length=255, blank=True)
    country = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50, blank=True)
    zip = models.CharField(max_length=5, blank=True)
    identity_number = models.CharField(max_length=9, blank=False)


class ClientProfile(UserProfile):
    photo = models.ImageField(upload_to='uploads', blank=True, null=True)


class OwnerProfile(UserProfile):
    license_number = models.CharField(max_length=255)

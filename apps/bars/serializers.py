from rest_framework import serializers
from django.contrib.auth import get_user_model
from apps.accounts.serializers import UserSerializer
from .models import Bar


class BarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bar
        fields = ("name", "address", "capacity", "logo")
        read_only_fields = ("id",)


class BarDetailSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)

    class Meta:
        model = Bar
        fields = '__all__'
        read_only_fields = ('id',)
        extra_kwargs = {'owner': {'required': False}}

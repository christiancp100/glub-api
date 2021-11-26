from rest_framework import serializers
from django.contrib.auth import get_user_model
from apps.accounts.serializers import UserSerializer
from .models import Bar, BarImage


class BarImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BarImage
        fields = ("bar", "image", "description")


class BarSerializer(serializers.ModelSerializer):
    images = BarImageSerializer(many=True, read_only=True)

    class Meta:
        model = Bar
        fields = ("name", "address", "capacity", "logo", "images")
        read_only_fields = ("id",)


class BarDetailSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    images = BarImageSerializer(many=True, read_only=True)

    class Meta:
        model = Bar
        fields = '__all__'
        read_only_fields = ('id',)
        extra_kwargs = {'owner': {'required': False}}

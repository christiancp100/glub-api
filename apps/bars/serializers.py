from rest_framework import serializers
from apps.accounts.serializers import UserSerializer
from .models import Bar, BarImage


class BarImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BarImage
        fields = "__all__"


class BarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bar
        fields = ("id", "name", "address", "capacity", "logo")
        read_only_fields = ("id",)


class BarDetailSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    images = BarImageSerializer(source="barimage_set", many=True, read_only=True)

    class Meta:
        model = Bar
        fields = '__all__'
        read_only_fields = ('id',)
        extra_kwargs = {'owner': {'required': False}}

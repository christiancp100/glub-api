from rest_framework import serializers
from apps.bars.models import Bar
from apps.accounts.serializers import UserSerializer


class BarSerializer(serializers.ModelSerializer):
    owner_id = serializers.CharField(source="owner.id")

    class Meta:
        model = Bar
        fields = ("owner_id", "name", "address", "capacity",)
        read_only_fields = ("id",)


class BarDetailSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)

    class Meta:
        model = Bar
        fields = '__all__'
        read_only_fields = ('id',)
        extra_kwargs = {'owner': {'required': False}}
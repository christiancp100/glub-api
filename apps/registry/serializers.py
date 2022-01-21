from rest_framework import serializers
from apps.accounts.serializers import UserSerializer
from apps.bars.serializers import BarSerializer
from .models import Registry


class RegistrySerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    bar = BarSerializer(read_only=True)

    class Meta:
        model = Registry
        fields = '__all__'
        read_only_fields = ('id',)





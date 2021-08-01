from rest_framework import serializers
from apps.bars.models import Bar
from django.contrib.auth import get_user_model
from apps.accounts.serializers import UserSerializer


class BarSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)

    class Meta:
        model = Bar
        fields = '__all__'
        read_only_fields = ('id',)
        extra_kwargs = {'owner': {'required': False}}

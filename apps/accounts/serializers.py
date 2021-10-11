from .models import User
from rest_framework import serializers
from django.core.validators import EmailValidator
from .models.user import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        read_only_fields = ('id',)
        optional_fields = '__all__'
        exclude = ('user',)


class BaseUserSerializer(serializers.HyperlinkedModelSerializer):
    profile = UserProfileSerializer(required=True)

    class Meta:
        model = User
        extra_kwargs = {'email': {'validators': [EmailValidator, ]}}


class PartialUserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = ['id', 'email', 'first_name', 'last_name', 'profile']
        extra_kwargs = {'email': {'validators': [EmailValidator, ]}}

    def save_partial(self, validated_data):
        user = User.objects.create_partial_user(**validated_data)
        return user.id

    def update(self, instance, validated_data):
        profile = validated_data.pop("profile", None)
        UserProfile.objects.update(**profile)
        user_id = User.objects.filter(id=instance.id).update(**validated_data)
        return user_id


class UserSerializer(BaseUserSerializer):
    profile = UserProfileSerializer(required=True)

    class Meta(BaseUserSerializer.Meta):
        fields = ['id', 'email', 'first_name', 'last_name', 'password', 'profile']
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {
                    'input_type': 'password'
                }
            }
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

from .models import User
from rest_framework import serializers

from .models.user import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        read_only_fields = ('id',)
        optional_fields = '__all__'
        exclude = ('user',)

    def validate_identity_number(self, identity_number):
        if len(identity_number) < 9:
            raise serializers.ValidationError("El DNI está mal escrito.")
        return identity_number


class BaseUserSerializer(serializers.HyperlinkedModelSerializer):
    profile = UserProfileSerializer(required=True)

    class Meta:
        model = User


class PartialUserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = ['id', 'email', 'first_name', 'last_name', 'profile']

    def save_partial(self, validated_data):
        user = User.objects.create_partial_user(**validated_data)
        return user


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

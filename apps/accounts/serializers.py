from .models import User
from rest_framework import routers, serializers, viewsets, permissions
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models.user import UserManager, UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        read_only_fields = ('id',)
        optional_fields = '__all__'
        exclude = ('user',)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    profile = UserProfileSerializer(required=True)

    class Meta:
        model = User
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

    def update(self, instance, validated_data):
        print("Viene a este método", instance.id)

        profile_data = validated_data.pop('profile')
        UserProfile.objects.update(user_id=instance.id, **profile_data)
        if 'password' in validated_data:
            password = validated_data.pop('password', None)
            instance.set_password(password)
        return super().update(instance, validated_data)

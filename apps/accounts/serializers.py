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

    def validate_identity_number(self, value):
        if len(value) < 9:
            raise serializers.ValidationError("El DNI está mal escrito.")

    def get_identity_number(self, identity_number):
        print("hola: ", identity_number)
        return identity_number.upper()


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

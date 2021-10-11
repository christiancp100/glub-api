from rest_framework import status
from rest_framework.generics import GenericAPIView, ListCreateAPIView
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.serializers import ValidationError
from apps.accounts.permissions import IsOwner
from .models import Registry
from .serializers import RegistrySerializer
from apps.accounts.serializers import PartialUserSerializer
from apps.accounts.models import User
from apps.bars.models import Bar
from django.core.mail import send_mail
from django.conf import settings

def get_profile(data):
    try:
        phone = data.pop("phone")
        identity_number = data.pop("identity_number")
        data["profile"] = {
            "phone": phone,
            "identity_number": identity_number
        }
    except:
        raise ValidationError({"message": "El número de teléfono o el DNI no están presentes."})
    return data



class CreatePartialUserView(UpdateModelMixin, CreateModelMixin, GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = PartialUserSerializer

    def create(self, request, *args, **kwargs):
        user_data = get_profile(request.data)
        partial_user = self.serializer_class(data=user_data)
        if partial_user.is_valid(raise_exception=True):
            user = partial_user.save_partial(partial_user.validated_data)
            return user
        return ValidationError("Los datos no están bien escritos.")

    def update(self, request, *args, **kwargs):
        user_data = get_profile(request.data)
        serializer = self.serializer_class(data=user_data, partial=True)
        serializer.is_valid(raise_exception=True)
        user_id = serializer.update(User.objects.get(email=request.data.get("email", None)), serializer.data)
        return Response({"id": user_id})

    def post(self, request, *args, **kwargs):
        user = User.objects.filter(email=request.data.get("email", None)).first()
        if user is not None:
            user = self.update(request, *args, **kwargs)
        else:
            user = self.create(request, *args, **kwargs)
        send_mail(
            subject="Hola",
            message="Hola holita vecinito",
            from_email="info@glubapp.com",
            recipient_list=["christiancp100@gmail.com"],
            fail_silently=False
        )
        return user


class RegistryView(ListCreateAPIView):
    permission_classes = [IsOwner]
    serializer_class = RegistrySerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Registry.objects.all()
        elif self.request.user.is_owner:
            return Registry.objects.filter(bar__owner=self.request.user)

    def get(self, request, *args, **kwargs):
        registries = self.queryset
        serializer = RegistrySerializer(registries, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        user = User.objects.get(id=request.data.pop("user_id"))
        bar = Bar.objects.get(id=request.data.pop("bar_id"))
        if not user:
            return ValidationError("Este usuario no existe.")
        if not bar:
            return ValidationError("Este bar no existe.")
        serializer = RegistrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=user, bar=bar)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

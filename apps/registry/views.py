from rest_framework import status
from rest_framework.generics import GenericAPIView, ListCreateAPIView
from rest_framework.mixins import CreateModelMixin
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.serializers import ValidationError
from rest_framework.viewsets import ViewSet

from apps.accounts.models import User
from apps.accounts.permissions import IsOwner
from apps.accounts.serializers import PartialUserSerializer
from apps.bars.models import Bar
from utils.celery.tasks import send_mail_task

from .models import Registry
from .serializers import CapacitySerializer, RegistrySerializer


def get_profile(data):
    try:
        phone = data.pop("phone")
        identity_number = data.pop("identity_number")
        data["profile"] = {"phone": phone, "identity_number": identity_number}
    except:
        raise ValidationError("El número de teléfono o el DNI no están presentes.")
    return data


class CreatePartialUserView(CreateModelMixin, GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = PartialUserSerializer

    def create(self, request, *args, **kwargs):
        user_data = get_profile(request.data)
        partial_user = self.serializer_class(data=user_data)
        if partial_user.is_valid(raise_exception=True):
            user = partial_user.save_partial(partial_user.validated_data)
            return user
        return ValidationError("Los datos no están bien escritos.")

    def update(self, request, user, *args, **kwargs):
        user_data = get_profile(request.data)
        serializer = self.serializer_class(data=user_data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.update(user, serializer.data)
        return user

    def post(self, request, *args, **kwargs):
        user = User.objects.filter(email=request.data.get("email", None)).first()
        if user is not None:
            user = self.update(request, user, *args, **kwargs)
        else:
            user = self.create(request, *args, **kwargs)

        send_mail_task.delay(
            "Tu código QR ya está aquí",
            "registry/qr_code_email.html",
            "info@glubapp.com",
            [user.email],
            context={"user_id": user.id},
        )
        return Response(status=status.HTTP_200_OK)


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
            bar.increase_capacity()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CapacityView(ViewSet):
    permission_classes = [IsOwner]
    serializer_class = CapacitySerializer

    @staticmethod
    def decrease_capacity(request, *args, **kwargs):
        serializer = CapacitySerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            bar = Bar.objects.filter(id=serializer.data["bar_id"]).first()
            if bar:
                bar.decrease_capacity()
                return Response(
                    {"capacity": bar.capacity, "current_capacity": bar.current_capacity}
                )
            raise ValidationError("Debes especificar el bar_id")

    @staticmethod
    def increase_capacity(request, *args, **kwargs):
        serializer = CapacitySerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            bar = Bar.objects.filter(id=request.data.pop("bar_id", None)).first()
            if bar:
                bar.increase_capacity()
                return Response(
                    {"capacity": bar.capacity, "current_capacity": bar.current_capacity}
                )
        raise ValidationError("Debes especificar el bar_id")

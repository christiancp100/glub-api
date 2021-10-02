from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.serializers import ValidationError
from apps.bars.models import Bar
from apps.accounts.models.user import User
from apps.accounts.serializers import PartialUserSerializer


class CreatePartialUserView(CreateModelMixin, GenericAPIView):
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        partial_user = PartialUserSerializer(data=request.data)
        if partial_user.is_valid(raise_exception=True):
            id = partial_user.save_partial(partial_user.validated_data).id
            return Response({"id": id})
        return ValidationError("Los datos no están bien escritos.")

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

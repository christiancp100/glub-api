from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from apps.bars.models import Bar
from apps.bars.serializers import BarSerializer


@api_view(['POST'])
@permission_classes([AllowAny])
def create_partial_user(request):
    print(request.data)
    return Response(request.data)


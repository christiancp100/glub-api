from django.shortcuts import render
from rest_framework import status, mixins, generics
from rest_framework.response import Response

from .models import Bar
from .serializers import BarSerializer
# Create your views here.
from rest_framework.views import APIView

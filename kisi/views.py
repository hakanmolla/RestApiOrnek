from django.shortcuts import render
from rest_framework import viewsets,status,mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import kisiler
from .serializers import KisilerSerializer

# Create your views here.

class KisileriGosterViewSet(mixins.ListModelMixin,viewsets.GenericViewSet):
     queryset=kisiler.objects.all()
     serializer_class=KisilerSerializer

class KisiEkleAndGuncelleViewset(mixins.CreateModelMixin,mixins.UpdateModelMixin,viewsets.GenericViewSet):
     queryset=kisiler.objects.all()
     serializer_class=KisilerSerializer

class KisiSilViewSet(mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset=kisiler.objects.all()
    serializer_class=KisilerSerializer
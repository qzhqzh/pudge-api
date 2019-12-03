from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from demo.models import BasicDemo
from demo.serializers import BasicDemoSerializer


class BasicDemoViewSet(ModelViewSet):
    queryset = BasicDemo.objects.all()
    serializer_class = BasicDemoSerializer

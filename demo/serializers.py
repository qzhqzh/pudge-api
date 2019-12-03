from rest_framework.serializers import ModelSerializer
from demo.models import BasicDemo


class BasicDemoSerializer(ModelSerializer):
    class Meta:
        model = BasicDemo
        fields = '__all__'
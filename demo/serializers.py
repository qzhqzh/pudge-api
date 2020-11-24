from rest_framework.serializers import ModelSerializer
from demo.models import BasicDemo, FileUploadDemo


class BasicDemoSerializer(ModelSerializer):
    class Meta:
        model = BasicDemo
        fields = '__all__'

class FileUploadDemoSerializer(ModelSerializer):
    class Meta:
        model = FileUploadDemo
        fields = '__all__'

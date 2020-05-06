from .models import *
from rest_framework import serializers


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'

    def get_fields(self):
        fields = super(NoteSerializer, self).get_fields()
        if self.context['request'].method == 'GET':
            fields['last_upload'] = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
            fields['last_backup'] = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
            return fields
        return fields

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'



class StatusDisplaySerialzier(object):
    def get_status_display(self, obj):
        return obj.get_status_display()


class TodoSerializer(serializers.ModelSerializer, StatusDisplaySerialzier):
    class Meta:
        model = Todo
        fields = '__all__'

    def get_fields(self):
        fields = super(TodoSerializer, self).get_fields()
        if self.context['request'].method == 'GET':
            fields['status_display'] = serializers.SerializerMethodField()
            return fields
        return fields


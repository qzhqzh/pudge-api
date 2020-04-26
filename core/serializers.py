from rest_framework import serializers
from core.models import Attachement


class AttachmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Attachement
        fields = '__all__'
        # extra_kwargs = {
        #
        # }
from rest_framework import serializers
from core.models import Attachment


class AttachmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Attachment
        fields = '__all__'
        # extra_kwargs = {
        #
        # }
from rest_framework.viewsets import ModelViewSet
from core.models import Attachment
from core.serializers import AttachmentSerializer


class AttachmentViewSet(ModelViewSet):
    queryset = Attachment.objects.all()
    serializer_class = AttachmentSerializer


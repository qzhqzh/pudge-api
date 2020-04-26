from rest_framework.viewsets import ModelViewSet
from core.models import Attachement
from core.serializers import AttachmentSerializer


class AttachmentViewSet(ModelViewSet):
    queryset = Attachement.objects.all()
    serializer_class = AttachmentSerializer


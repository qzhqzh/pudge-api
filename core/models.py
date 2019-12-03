from django.db import models
from django.utils import timezone
from softdelete.models import SoftDeleteObject
from model_utils.models import StatusModel
import uuid


# Create your models here
class UuidModel(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4,
                          editable=False, verbose_name='唯一UUID')

    class Meta:
        abstract = True

class CoreModel(UuidModel):
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


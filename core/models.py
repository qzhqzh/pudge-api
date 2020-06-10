from django.db import models
from django.utils import timezone
from softdelete.models import SoftDeleteObject
from model_utils.models import StatusModel
from django.contrib.auth.models import AbstractUser, User, Group, UserManager
from django.contrib.postgres import fields
import uuid


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


class UserProfile(CoreModel):
    user = models.OneToOneField(User, related_name='profile',
                                on_delete=models.CASCADE)


class GroupProfile(CoreModel):
    group = models.OneToOneField(Group, related_name='group',
                                 on_delete=models.CASCADE)


class Attachment(CoreModel):
    model = models.CharField(max_length=255, blank=True, null=True)
    model_id = models.UUIDField(null=True)
    name = models.CharField(max_length=255, blank=True)
    file = models.FileField()
    comment = models.CharField(max_length=255, blank=True)


class Scan(CoreModel):
    filepath = models.CharField(max_length=255)

class Backup(CoreModel):
    ACTION = (
        ('backup', 'backup'),
        ('upload', 'upload')
    )
    action = models.CharField(max_length=255, choices=ACTION)


# class Setting(CoreModel):

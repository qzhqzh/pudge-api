from django.db import models
from core.models import CoreModel


# Create your models here.
class BasicDemo(CoreModel):
    name = models.CharField(max_length=512, verbose_name='测试字段')

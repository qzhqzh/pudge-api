from django.db import models
from core.models import CoreModel
from mdeditor.fields import MDTextField

# Create your models here.
class Article(CoreModel):
    title = models.CharField(max_length=128, verbose_name='文章标题')
    body = MDTextField(max_length=128, verbose_name='文章标题')

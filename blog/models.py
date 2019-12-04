from core.models import CoreModel
from mdeditor.fields import MDTextField, MDTextFormField
from django.db import models
from django import forms


# Create your models here.
class Article(CoreModel):
    title = models.CharField(max_length=128, verbose_name='文章标题')
    body = MDTextField(max_length=128, verbose_name='文章标题')

# Mdeditor models
class MDEditorForm(forms.Form):
    title = forms.CharField()
    body = MDTextFormField(config_name='form_config')

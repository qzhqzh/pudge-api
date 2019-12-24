from core.models import CoreModel
from mdeditor.fields import MDTextField, MDTextFormField
from django.db import models
from django import forms
from uuslug import slugify


class SlugModel(CoreModel):
    # name = models.CharField(max_length=30, verbose_name='名称', unique=True)
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(SlugModel, self).save(*args, **kwargs)

class Category(SlugModel):
    name = models.CharField(max_length=30, verbose_name='分类名称', unique=True)
    parent = models.ForeignKey('self', verbose_name='标签爸爸', blank=True,
                               null=True, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=40, blank=True)

class Tag(SlugModel):
    name = models.CharField(max_length=30, verbose_name='标签名称', unique=True)
    slug = models.SlugField(max_length=40, blank=True)

# Create your models here.
class Article(CoreModel):
    title = models.CharField(max_length=128, verbose_name='文章标题')
    body = MDTextField(max_length=128, verbose_name='文章标题')
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.CASCADE, verbose_name='文章分类')
    tags = models.ManyToManyField(Tag, blank=True, verbose_name='文章标签')


class Todo(CoreModel):
    GROUP_CHOICES = (
        (-1, 'cancer'),
        (0, 'waiting'),
        (1, 'running'),
        (2, 'finish')
    )
    body = MDTextField(max_length=128, verbose_name='内容')
    status = models.SmallIntegerField(verbose_name='状态', choices=GROUP_CHOICES)

    @property
    def aa(self):
        return self.status
    # def get_status_display(self):
    #     return dict(self.GROUP_CHOICES).get(self.status, 'error')

# Mdeditor Form
class ArticleMDEditorForm(forms.Form):
    title = forms.CharField()
    body = MDTextFormField(config_name='form_config')

class TodoMDEditorForm(forms.Form):
    body = MDTextFormField(config_name='form_config')
    status = forms.ChoiceField(choices=Todo.GROUP_CHOICES)


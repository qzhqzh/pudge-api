from django.db import models
from django import forms
from mdeditor.fields import MDTextField, MDTextFormField

from core.models import CoreModel, User
from uuslug import slugify

class Category(CoreModel):
    name = models.CharField(max_length=256, null=False, unique=True)
    parent = models.ForeignKey('self', verbose_name='分类爸爸', blank=True,
                               null=True, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=40, blank=True, null=True)

class Tag(CoreModel):
    name = models.CharField(max_length=256, null=False, unique=True)
    slug = models.SlugField(max_length=40, blank=True, null=True)

class Article(CoreModel):
    title = models.CharField(max_length=256, unique=True)
    content = models.TextField()

    class Meta:
        abstract = True


class SlugModel(CoreModel):
    # name = models.CharField(max_length=30, verbose_name='名称', unique=True)
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(SlugModel, self).save(*args, **kwargs)

class Note(Article):
    author = models.ForeignKey(User, related_name='notes',
                               on_delete=models.SET_NULL, blank=True, null=True)
    category = models.ForeignKey(Category, max_length=256, related_name='notes',
                                 on_delete=models.SET_NULL, blank=True,
                                 null=True)
    tags = models.ManyToManyField(Tag, related_name='notes', blank=True)

    def __str__(self):
        return '%s（%s）' % (
            self.title, '、'.join([tag.name for tag in self.tags.all()]))

class Blog(Article):
    author = models.ForeignKey(User, related_name='blogs',
                               on_delete=models.SET_NULL, blank=True, null=True)
    category = models.ForeignKey(Category, max_length=256, related_name='blogs',
                                 on_delete=models.SET_NULL, blank=True,
                                 null=True)
    tags = models.ManyToManyField(Tag, related_name='blogs', blank=True)

    def __str__(self):
        return '%s（%s）' % (
            self.title, '、'.join([tag.name for tag in self.tags.all()]))



class Todo(CoreModel):
    GROUP_CHOICES = (
        (-1, 'cancer'),
        (0, 'waiting'),
        (1, 'running'),
        (2, 'finish')
    )
    body = MDTextField(max_length=128, verbose_name='内容')
    status = models.SmallIntegerField(verbose_name='状态', choices=GROUP_CHOICES,
                                      )

    @property
    def aa(self):
        return self.status
    # def get_status_display(self):
    #     return dict(self.GROUP_CHOICES).get(self.status, 'error')


# Mdeditor Form
class ArticleMDEditorForm(forms.Form):
    title = forms.CharField()
    body = MDTextFormField(config_name='form_config')
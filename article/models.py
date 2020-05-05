from django.db import models
from django import forms
from mdeditor.fields import MDTextField, MDTextFormField

from core.models import CoreModel, User, Backup
from uuslug import slugify

import os


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
    content = models.TextField(blank=True)

    class Meta:
        abstract = True


class SlugMixin(object):
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super(SlugMixin, self).save(*args, **kwargs)


# class VersionMixin(object):


class Note(Article, SlugMixin):
    author = models.ForeignKey(User, related_name='notes',
                               on_delete=models.SET_NULL, blank=True, null=True)
    category = models.ForeignKey(Category, max_length=256, related_name='notes',
                                 on_delete=models.SET_NULL, blank=True,
                                 null=True)
    tags = models.ManyToManyField(Tag, related_name='notes', blank=True)
    file = models.CharField(max_length=255, blank=True, null=True)
    backups = models.ManyToManyField(Backup, related_name='notes', blank=True)

    def __str__(self):
        return '%s（%s）' % (
            self.title, '、'.join([tag.name for tag in self.tags.all()]))

    @property
    def extension(self):
        filename, extension = os.path.splitext(self.file)
        return extension

    @property
    def last_upload(self):
        if self.backups.filter(action='upload').exists():
            return self.backups.filter(action='upload').order_by(
                '-created_at').first().created_at
        return None

    @property
    def last_backup(self):
        if self.backups.filter(action='backup').exists():
            return self.backups.filter(action='backup').order_by(
                '-created_at').first().created_at
        return None



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

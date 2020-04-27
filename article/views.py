from django.shortcuts import redirect
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.reverse import reverse
from markdown import markdown
import os

from article.models import Note, Blog
from article.serializers import NoteSerializer, BlogSerializer
from core.models import Attachment
from core.serializers import AttachmentSerializer


class NoteViewSet(ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

class BlogViewSet(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer



class NoteAPIViewSet(ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    renderer_classes = [TemplateHTMLRenderer]
    page = 'Note'

    def list(self, request, *args, **kwargs):
        self.template_name = 'article/note-list.html'
        resp = super(NoteAPIViewSet, self).list(request, *args, **kwargs)
        return Response({'notes': resp.data, 'page': self.page})

    def retrieve(self, request, *args, **kwargs):
        self.template_name = 'article/note-detail.html'
        resp = super(NoteAPIViewSet, self).retrieve(request, *args, **kwargs)
        content_html = markdown(resp.data['content'])
        return Response({'note': resp.data, 'page': self.page, 'content_html': content_html})

    @action(methods=['get'], detail=False)
    def new(self, request, *args, **kwargs):
        self.template_name = 'article/note-new.html'
        return Response({'page': 'Note'})


    @action(methods=['get'], detail=False)
    def upload(self, request, *args, **kwargs):
        self.template_name = 'article/note-upload.html'
        return Response({'page': 'Note'})

    @action(methods=['post'], detail=False)
    def uploadnew(self, request, *args, **kwargs):
        self.queryset = Attachment.objects.all()
        self.serializer_class = AttachmentSerializer

        resp = NoteViewSet.create(self, request, *args, **kwargs)
        attachment_id = resp.data['id']
        attachment = Attachment.objects.get(id=attachment_id)
        title, extension = os.path.splitext(attachment.file.name)
        with open(attachment.file.path)as fh:
            content = fh.read()
        note = Note.objects.create(title=title,
                            content=content)
        attachment.model = 'article.note'
        attachment.model_id = note.id
        attachment.save()
        return redirect(reverse('t-note-list'))

    def create(self, request, *args, **kwargs):
        super(NoteAPIViewSet, self).create(request, *args, **kwargs)
        return redirect(reverse('t-note-list'))

    @action(methods=['get'], detail=True)
    def edit(self, request, *args, **kwargs):
        resp = self.retrieve(request, *args, **kwargs)
        self.template_name = 'article/note-edit.html'
        return resp


class BlogAPIViewSet(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    renderer_classes = [TemplateHTMLRenderer]

    def list(self, request, *args, **kwargs):
        self.template_name = 'article/blog-list.html'
        queryset = self.get_queryset()
        return Response({'blogs': queryset, 'page': 'Blog'})

    def retrieve(self, request, *args, **kwargs):
        self.template_name = 'article/blog-detail.html'
        queryset = self.get_queryset()
        return Response({'blog': queryset, 'page': 'Blog'})



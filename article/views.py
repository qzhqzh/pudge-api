from django.shortcuts import redirect
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.reverse import reverse
from markdown import markdown

from article.models import Note, Blog
from article.serializers import NoteSerializer, BlogSerializer


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



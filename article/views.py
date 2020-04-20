from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from article.models import Note, Blog
from article.serializers import NoteSerializer, BlogSerializer


class NoteViewSet(ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

class NoteAPIViewSet(ModelViewSet):
    queryset = Note.objects.all()
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'article/note-list.html'

    def list(self, request):
        queryset = self.get_queryset()
        return Response({'notes': queryset})

class BlogViewSet(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class BlogAPIViewSet(ModelViewSet):
    queryset = Blog.objects.all()
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'article/blog-list.html'

    def list(self, request):
        queryset = self.get_queryset()
        return Response({'blogs': queryset})
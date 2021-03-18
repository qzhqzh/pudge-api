from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

# Create your views here.
from kbms.models import Article
from kbms.serializers import ArticleSerializer


def editor(request):
    return render(request, 'editor.html', {'page': 'Editor'})






# restful-viewsets

class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

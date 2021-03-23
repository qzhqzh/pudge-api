from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

# Create your views here.
from kbms.models import Article
from kbms.serializers import ArticleSerializer


class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [AllowAny,]

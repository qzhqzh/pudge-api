from django.shortcuts import render
from blog.models import Article
import markdown


def index(request):
    return render(request, 'index.html', {})

def app(request):
    return render(request, 'app.html', {})


def blog(request):
    return render(request, 'blog/index.html', {})

def article_detail(request, id):
    article = Article.objects.get(id=id)
    # 将markdown语法渲染成html样式
    article.body = markdown.markdown(article.body,
    extensions=[
        # 包含 缩写、表格等常用扩展
        'markdown.extensions.extra',
        # 语法高亮扩展
        'markdown.extensions.codehilite',
        #允许我们自动生成目录
        'markdown.extensions.toc',
    ])
    context = { 'article': article }
    return render(request, 'blog/article-detail.html', context)
from django.shortcuts import render
from django.views.generic import View
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_protect
from blog.models import Article, MDEditorForm
import markdown


def index(request):
    return render(request, 'index.html', {})

def app(request):
    return render(request, 'app.html', {})


def article_list(request):
    articles = Article.objects.all().values('id', 'title',)
    return render(request, 'blog/article-list.html', {'articles': articles})

class ArticleNewView(View):

    def get(self, request, *args, **kwargs):
        form = MDEditorForm()
        return render(request, 'blog/article-new.html', {'form': form})

    def post(self, request, *args, **kwargs):
        title = request.POST.get('title')
        body = request.POST.get('body')
        article = Article.objects.create(title=title, body=body)
        article.body = markdown.markdown(article.body,
                                         extensions=[
                                             # 包含 缩写、表格等常用扩展
                                             'markdown.extensions.extra',
                                             # 语法高亮扩展
                                             'markdown.extensions.codehilite',
                                             # 允许我们自动生成目录
                                             'markdown.extensions.toc',
                                         ])
        return render(request, 'blog/article-detail.html', {'article': article})

def article_detail(request, *args, **kwargs):
    article_id = kwargs.get('article_id')
    if not article_id:
        return HttpResponseBadRequest('necessary param: article_id')
    article = Article.objects.get(id=article_id)
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

class ArticleEditView(View):
    def get(self, request, *args, **kwargs):
        article_id = kwargs.get('article_id')
        article = Article.objects.get(id=article_id)
        form = MDEditorForm(initial={'title': article.title, 'body': article.body})
        return render(request, 'blog/article-edit.html', {'form': form, 'article': article})

    def post(self, request, *args, **kwargs):
        article_id = kwargs.get('article_id')
        title = request.POST.get('title')
        body = request.POST.get('body')
        Article.objects.filter(id=article_id).update(title=title, body=body)
        article = Article.objects.get(id=article_id)
        article.body = markdown.markdown(article.body,
                                         extensions=[
                                             # 包含 缩写、表格等常用扩展
                                             'markdown.extensions.extra',
                                             # 语法高亮扩展
                                             'markdown.extensions.codehilite',
                                             # 允许我们自动生成目录
                                             'markdown.extensions.toc',
                                         ])
        return render(request, 'blog/article-detail.html', { 'article': article })

    def delete(self, request, *args, **kwargs):
        article_id = kwargs.get('article_id')
        Article.objects.filter(id=article_id).delete()
        return HttpResponse('%s has successful deleted' % article_id, status=204)

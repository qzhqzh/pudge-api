from django.views.generic import View
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_protect
from blog.models import Article, Category, Tag, ArticleMDEditorForm, Todo, TodoMDEditorForm
from blog.serializers import ToDoSerializer
import markdown
import re
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, ListModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer, BrowsableAPIRenderer
from rest_framework.response import Response
from rest_framework.decorators import action
from django.http import HttpResponseRedirect
from rest_framework.reverse import reverse
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


def article_list(request):
    articles = Article.objects.all().values('id', 'title',)
    return render(request, 'blog/article-list.html', {'articles': articles})

class ArticleNewView(View):

    def get(self, request, *args, **kwargs):
        form = ArticleMDEditorForm()
        return render(request, 'blog/article-new.html', {'form': form})

    def post(self, request, *args, **kwargs):
        title = request.POST.get('title')
        body = request.POST.get('body')

        category_name = request.POST.get('category')
        tag_names = request.POST.get('tags')
        tag_names = re.split(r'[,;\s|]', tag_names)

        category, is_exists = Category.objects.get_or_create(name=category_name)
        tags = []
        for tag_name in tag_names:
            tag, is_exists = Tag.objects.get_or_create(name=tag_name)
            tags.append(tag.id)

        article = Article.objects.create(title=title, body=body, category=category)
        article.tags.add(*tags)
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
        form = ArticleMDEditorForm(initial={'title': article.title, 'body': article.body})
        return render(request, 'blog/article-edit.html', {'form': form, 'article': article})

    def post(self, request, *args, **kwargs):
        article_id = kwargs.get('article_id')
        title = request.POST.get('title')
        body = request.POST.get('body')

        category_name = request.POST.get('category')
        tag_names = request.POST.get('tags')
        tag_names = re.split(r'[,;\s|]', tag_names)

        category, is_exists = Category.objects.get_or_create(name=category_name)
        tags = []
        for tag_name in tag_names:
            tag, is_exists = Tag.objects.get_or_create(name=tag_name)
            tags.append(tag.id)


        Article.objects.filter(id=article_id).update(title=title, body=body, category=category)
        article = Article.objects.get(id=article_id)
        article.tags.add(*tags)
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


class ToDoAPIViewSet(GenericViewSet, CreateModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = Todo.objects.all()
    serializer_class = ToDoSerializer
    permission_classes = []

    @method_decorator(login_required(login_url='/api-auth/login'))
    @action(['POST'], detail=True)
    def edit(self, request, *args, **kwargs):
        resp = super(ToDoAPIViewSet, self).update(request, *args, **kwargs)
        todo = resp.data
        return HttpResponseRedirect(reverse('todo-detail', kwargs={'pk': todo['id']}))

    @method_decorator(login_required(login_url='/api-auth/login'))
    def create(self, request, *args, **kwargs):
        resp = super(ToDoAPIViewSet, self).create(request, *args, **kwargs)
        todo = resp.data
        return HttpResponseRedirect(reverse('todo-detail', kwargs={'pk': todo['id']}))


class ToDoHtmlViewSet(GenericViewSet, RetrieveModelMixin, ListModelMixin):
    queryset = Todo.objects.all()
    serializer_class = ToDoSerializer
    renderer_classes = [TemplateHTMLRenderer]

    def retrieve(self, request, *args, **kwargs):
        todo = self.get_object()
        resp = super(ToDoHtmlViewSet, self).retrieve(request, *args, **kwargs)
        return Response({'todo': todo, 'serializer': resp},
                        template_name='blog/todo-detail.html')

    def list(self, request, *args, **kwargs):
        resp = super(ToDoHtmlViewSet, self).list(request, *args, **kwargs)
        return Response({'todo_list': resp.data},
                        template_name='blog/todo-list.html')

    @method_decorator(login_required(login_url='/api-auth/login'))
    @action(['GET'], detail=False)
    def new(self, request, *args, **kwargs):
        form = TodoMDEditorForm()
        return render(request, 'blog/todo-new.html', {'form': form})

    # @action(['POST'], detail=True)
    # def edit(self, request, *args, **kwargs):
    #     todo = self.get_object()
    #     form = ArticleMDEditorForm(initial={'body': todo.body,
    #                                         'status': todo.status})
    #     return render(request, 'blog/todo-edit.html', {'form': form, 'article': todo})

    # renderer_classes = [TemplateHTMLRenderer, JSONRenderer, BrowsableAPIRenderer]

    # def retrieve(self, request, *args, **kwargs):
    #     # print(self.renderer_classes)
    #     # self.renderer_classes = [JSONRenderer]
    #     # print(self.renderer_classes)
    #     self.template_name = 'blog/todo-detail.html'
    #     resp = super(ToDoViewSet, self).retrieve(request, *args, **kwargs)
    #     return Response({'todo': resp.data, 'serializer':resp}, template_name='blog/todo-detail.html')

    # def list(self, request, *args, **kwargs):
    #     # print(self.renderer_classes)
    #     # self.renderer_classes = [JSONRenderer]
    #     # print(self.renderer_classes)
    #
    #     resp = super(ToDoViewSet, self).list(request, *args, **kwargs)
    #     # self.template_name = 'blog/todo-list.html'
    #     # return render(request, 'blog/todo-list.html', {'todo_list': resp.data})
    #     return Response({'todo_list': resp.data}, template_name='blog/todo-list.html')
    #
    # def create(self, request, *args, **kwargs):
    #     self.renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    #     return super(ToDoViewSet, self).create(request, *args, **kwargs)
    #
    # def update(self, request, *args, **kwargs):
    #     self.renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    #     return super(ToDoViewSet, self).update(request, *args, **kwargs)
    #
    # def destroy(self, request, *args, **kwargs):
    #     self.renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    #     return super(ToDoViewSet, self).destroy(request, *args, **kwargs)


# class ToDoAPIViewSet(ModelViewSet):
#     queryset = Todo.objects.all()
#     serializer_class = ToDoSerializer
#
#     def get_queryset(self):
#         print(self.renderer_classes)
#         return super(ToDoAPIViewSet, self).get_queryset()
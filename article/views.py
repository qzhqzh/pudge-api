from django.shortcuts import redirect
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.reverse import reverse
from markdown import markdown
import os, math

from article.models import Note, Blog, Todo
from article.serializers import NoteSerializer, BlogSerializer, TodoSerializer
from core.models import Attachment, Backup
from core.serializers import AttachmentSerializer

from rest_framework.pagination import PageNumberPagination
from config.envs import BACKUP_DIR, SCAN_DIRS
from core.models import Scan


from django.contrib import messages

class StandardPageNumberPagination(PageNumberPagination):
    page_size_query_param = 'page_size'
    max_page_size = 1


from rest_framework.pagination import PageNumberPagination


class ArticlePagination(PageNumberPagination):
    page_size = 2  # 表示每页的默认显示数量
    page_size_query_param = 'page_size'  # 表示url中每页数量参数
    # page_query_param = 'page' # 表示url中的页码参数
    max_page_size = 100  # 表示每页最大显示数量，做限制使用，避免突然大量的查询数据，数据库崩溃


class MetaPageNumberPagination(PageNumberPagination):
    """ Create by admin@kuddy.cn
    """
    page_size_query_param = 'page_size'

    @property
    def view(self):
        return self._view

    def paginate_queryset(self, queryset, request, view=None):
        res = super(MetaPageNumberPagination, self).paginate_queryset(queryset,
                                                                      request,
                                                                      view)
        self._view = view
        return res

    def get_paginated_response(self, data):
        response = super(MetaPageNumberPagination, self).get_paginated_response(
            data)
        if hasattr(self.view, 'paginated_response_meta'):
            data = {
                'meta': self.view.paginated_response_meta()
            }
            data.update(response.data)
            response.data = data
        return response


class NoteViewSet(ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    pagination_class = MetaPageNumberPagination
    page = 'note'

    def paginated_response_meta(self):
        return {
            'page': self.page,
            'current_user': self.request.user.username
        }


class BlogViewSet(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class NoteHTMLViewSet(ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    renderer_classes = [TemplateHTMLRenderer]
    page = 'Note'
    pagination_class = MetaPageNumberPagination

    def paginated_response_meta(self):
        return {
            'page': self.page,
            'current_user': self.request.user.username
        }

    def list(self, request, *args, **kwargs):
        from config.settings import REST_FRAMEWORK
        self.template_name = 'article/note-list.html'
        resp = super(NoteHTMLViewSet, self).list(request, *args, **kwargs)
        current_page = self.request.query_params.get('page', 1)
        total_page = math.ceil(resp.data['count'] / REST_FRAMEWORK['PAGE_SIZE'])

        data = {
            'notes': resp.data['results'],
            'count': resp.data['count'],
            'current_page': current_page,
            'total_page': total_page,
            'previous': resp.data['previous'],
            'next': resp.data['next'],
            'page': resp.data['meta']['page'],
            'current_user': resp.data['meta']['current_user']
        }
        return Response(data)

    def retrieve(self, request, *args, **kwargs):
        self.template_name = 'article/note-detail.html'
        resp = super(NoteHTMLViewSet, self).retrieve(request, *args, **kwargs)
        content_html = markdown(resp.data['content'],
                                extensions=[
                                    'markdown.extensions.extra',
                                    'markdown.extensions.codehilite',
                                    'markdown.extensions.toc',
                                    'fenced_code'
                                ]
                                )
        return Response({'note': resp.data, 'page': self.page,
                         'content_html': content_html})

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
        print(1)
        try:
            super(NoteHTMLViewSet, self).create(request, *args, **kwargs)
        except Exception as e:
            print(e)
        print(2)
        return redirect(reverse('t-note-list'))

    @action(methods=['get'], detail=True)
    def edit(self, request, *args, **kwargs):
        resp = self.retrieve(request, *args, **kwargs)
        self.template_name = 'article/note-edit.html'
        return resp

    @action(methods=['get'], detail=True)
    def backup(self, request, *args, **kwargs):
        obj = self.get_object()

        # 不是第一次备份，且
        if obj.last_backup is not None and obj.last_backup > obj.last_upload:
            messages.add_message(request, messages.INFO, 'Hello world.')
            return redirect(reverse('t-note-list'))

        if not obj.file:
            obj.file = '%s.%s'%(obj.title, 'md')
            obj.save()
        with open(os.path.join(BACKUP_DIR, obj.file), 'w',
                  encoding='utf-8')as fhO:
            fhO.write(obj.content)
        backup = Backup.objects.create(action='backup')
        obj.backups.add(backup)

        return redirect(reverse('t-note-list'))

    def post2db(self, file, model):
        from django.db.models import Model
        if not issubclass(model, (Model,)) or not hasattr(model,
                                                          'title') or not hasattr(
                model, 'content'):
            return
        if file.endswith('md'):
            with open(file, encoding='utf-8')as fh:
                content = fh.read()
            filename = os.path.basename(file)
            title, extension = os.path.splitext(filename)


            note, is_create = model.objects.update_or_create(
                title=title,
                defaults={
                    "content": content,
                    "file": filename
                }
            )
            backup = Backup.objects.create(action='upload')
            note.backups.add(backup)

    @action(methods=['get'], detail=True)
    def sync(self, request, *args, **kwargs):
        obj = self.get_object()
        self.post2db(os.path.join(BACKUP_DIR,obj.file), Note)
        return redirect(reverse('t-note-list'))

    @action(methods=['get'], detail=False)
    def scan(self, request, *args, **kwargs):
        # todo: 嵌套目录的情况需要处理
        for scan_dir in SCAN_DIRS:
            for filename in os.listdir(scan_dir):
                filepath = os.path.join(scan_dir, filename)
                if not Scan.objects.filter(filepath=filepath).exists():
                    self.post2db(filepath, Note)
                    Scan.objects.create(filepath=filepath)
        return redirect(reverse('t-note-list'))


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



class HtmlDocumentViewSet(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    pagination_class = MetaPageNumberPagination
    renderer_classes = [TemplateHTMLRenderer]

    def list(self, request, *args, **kwargs):
        resp = super(HtmlDocumentViewSet, self).list(request, *args, **kwargs)
        data = {
            'resp': resp.data,
            'page': 'Document'
        }
        self.template_name = 'article/document-list.html'
        print(data)
        return Response(data)

class TodoViewSet(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    pagination_class = MetaPageNumberPagination

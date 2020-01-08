from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from demo.models import *
from demo.serializers import BasicDemoSerializer
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer, BrowsableAPIRenderer
from rest_framework.response import Response


class BasicDemoViewSet(ModelViewSet):
    queryset = BasicDemo.objects.all()
    serializer_class = BasicDemoSerializer

class Bootstrap4DemoViewSet(ModelViewSet):
    queryset = BasicDemo.objects.all()
    serializer_class = BasicDemoSerializer
    renderer_classes = [TemplateHTMLRenderer]
    
    def retrieve(self, request, *args, **kwargs):
        resp = super(Bootstrap4DemoViewSet, self).retrieve(request, *args, **kwargs)
        form = MyForm()
        return render(request, template_name='demo-bootstrap4.html', context={'form': form})


class HtmlDemoViewSet(ModelViewSet):
    queryset = BasicDemo.objects.all()
    serializer_class = BasicDemoSerializer
    renderer_classes = [TemplateHTMLRenderer]

    def retrieve(self, request, *args, **kwargs):
        resp = super(HtmlDemoViewSet, self).retrieve(request, *args,
                                                           **kwargs)
        return render(request, template_name='demo-html.html')

from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, ListModelMixin, UpdateModelMixin, DestroyModelMixin

class MDDemoViewSet(GenericViewSet, RetrieveModelMixin, ListModelMixin):
    queryset = BasicDemo.objects.all()
    serializer_class = BasicDemoSerializer
    renderer_classes = [TemplateHTMLRenderer]

    def list(self, request, *args, **kwargs):
        # resp = super(MDDemoViewSet, self).retrieve(request, *args,
        #                                                    **kwargs)
        # return render(request, template_name='demo-mdedit.html')

        return Response({}, template_name='demo-mdedit.html')

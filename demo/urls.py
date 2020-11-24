from django.conf.urls import url
from rest_framework import routers

from demo import views
from demo.views import *


router = routers.SimpleRouter(trailing_slash=False)
router.register(r'basic-demo', BasicDemoViewSet)
router.register(r'bootstrap4-html-demo', Bootstrap4DemoViewSet)
router.register(r'html-demo', HtmlDemoViewSet)
router.register(r'md-demo', MDDemoViewSet)

router.register(r'file-upload-demo', FileUploadDemoViewSet)

urlpatterns = router.urls

urlpatterns = urlpatterns + [
    url(r'test', views.test)
]

import mistune
mistune.Renderer()

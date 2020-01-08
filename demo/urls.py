from rest_framework import routers
from demo.views import *


router = routers.SimpleRouter(trailing_slash=False)
router.register(r'basic-demo', BasicDemoViewSet)
router.register(r'bootstrap4-html-demo', Bootstrap4DemoViewSet)
router.register(r'html-demo', HtmlDemoViewSet)
router.register(r'md-demo', MDDemoViewSet)
urlpatterns = router.urls


import mistune
mistune.Renderer()

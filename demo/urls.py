from rest_framework import routers
from demo.views import BasicDemoViewSet


router = routers.SimpleRouter(trailing_slash=False)
router.register(r'basic-demo', BasicDemoViewSet)
urlpatterns = router.urls

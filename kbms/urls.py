from rest_framework import routers

from kbms.views import ArticleViewSet

router = routers.SimpleRouter(trailing_slash=False)
router.register(r'article', ArticleViewSet, basename='kbms-article')
urlpatterns = router.urls

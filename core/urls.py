from rest_framework import routers

from core.views import AttachmentViewSet


router = routers.SimpleRouter(trailing_slash=False)
router.register('attachment', AttachmentViewSet, basename='attachment')
urlpatterns = router.urls
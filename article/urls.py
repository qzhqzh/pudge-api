from rest_framework import routers
from .views import NoteViewSet, NoteHTMLViewSet, BlogViewSet, BlogAPIViewSet


router = routers.SimpleRouter(trailing_slash=False)
router.register('note', NoteViewSet, base_name='note')
router.register('t-note', NoteHTMLViewSet, base_name='t-note')
router.register('blog', BlogViewSet, base_name='blog')
router.register('t-blog', BlogAPIViewSet, base_name='t-blog')
urlpatterns = router.urls
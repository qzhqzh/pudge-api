from rest_framework import routers
from .views import NoteViewSet, NoteHTMLViewSet, BlogViewSet, BlogAPIViewSet, HtmlDocumentViewSet, TodoViewSet


router = routers.SimpleRouter(trailing_slash=False)
router.register('note', NoteViewSet, basename='note')
router.register('t-note', NoteHTMLViewSet, basename='t-note')
router.register('blog', BlogViewSet, basename='blog')
router.register('t-blog', BlogAPIViewSet, basename='t-blog')

router.register('t-document', HtmlDocumentViewSet, basename='t-document')
router.register('todo', TodoViewSet, basename='todo')
urlpatterns = router.urls
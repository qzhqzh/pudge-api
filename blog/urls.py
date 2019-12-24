from rest_framework import routers
from blog.views import *


router = routers.SimpleRouter(trailing_slash=False)
router.register('/todo', ToDoHtmlViewSet, base_name='todo')
router.register('/api/todo', ToDoAPIViewSet, base_name='todo-api')
urlpatterns = router.urls

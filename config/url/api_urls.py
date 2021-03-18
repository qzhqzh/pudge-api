from django.urls import path, include
from django.contrib import admin

api_urlpatterns = [
    # core
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    # api
    # path('api/blog/', include('blog.urls')),
    # path('api/note/', include('note.urls')),
    path('api/article/', include('article.urls')),
    path('api/core/', include('core.urls')),
    path('api/kbms/', include('kbms.urls')),
    # path('api/demo/', include('demo.urls')),
]

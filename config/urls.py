"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include
from django.conf.urls import url

from django.contrib import admin
from django.conf.urls.static import static
from config import settings
from config.views import index, mylogin, mylogout
from blog.views import *
# import blog.urls
# import demo.urls
from django.contrib.auth.decorators import login_required
from rest_framework.documentation import include_docs_urls


urlpatterns = [
    # core
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('mdeditor/', include('mdeditor.urls')),

    # template
    path('', index, name='home'),
    path('login', mylogin, name='login'),
    path('logout', mylogout, name='logout'),
    # path('blog/article', article_list, name='article_list'),
    # path('blog/article/new', login_required(ArticleNewView.as_view(), login_url='/api-auth/login'), name='article_new'),
    # path('blog/article/<uuid:article_id>', article_detail, name='article_detail'),
    # path('blog/article/<uuid:article_id>/edit', login_required(ArticleEditView.as_view(), login_url='/api-auth/login'), name='article_edit'),
    # # path('blog/todo', todo_list, name='todo_list'),
    # path('blog/article/new', login_required(ArticleNewView.as_view(), login_url='/api-auth/login'), name='article_new'),
    # path('blog/article/<uuid:article_id>', article_detail, name='article_detail'),
    # path('blog/article/<uuid:article_id>/edit', login_required(ArticleEditView.as_view(), login_url='/api-auth/login'), name='article_edit'),
    # path('api-demo/', include(demo.urls.urlpatterns)),
    # path('api/demo/', include('demo.urls')),
    # path('auth/', include('django.contrib.auth.urls')),  # 模板需要自己写

    # api
    # path('api/blog/', include('blog.urls')),
    # path('api/note/', include('note.urls')),
    path('api/article/', include('article.urls')),
    path('api/core/', include('core.urls')),

]

urlpatterns += [
    url("docs/", include_docs_urls(title="MY API DOCS")),
]

if settings.dev.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += static(settings.base.MEDIA_URL, document_root=settings.base.MEDIA_ROOT)

    from rest_framework import permissions
    from drf_yasg.views import get_schema_view
    from drf_yasg import openapi

    schema_view = get_schema_view(
        openapi.Info(
            title="Snippets API",
            default_version='v1',
            description="Test description",
            terms_of_service="https://www.google.com/policies/terms/",
            contact=openapi.Contact(email="contact@snippets.local"),
            license=openapi.License(name="BSD License"),
        ),
        public=True,
        permission_classes=(permissions.AllowAny,),
    )

    urlpatterns = [
        url(r'^swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),
        url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0),
            name='schema-swagger-ui'),
        url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0),
            name='schema-redoc'),
    ] + urlpatterns


    # https://www.cnblogs.com/yzxing/p/9409474.html
    import debug_toolbar

    urlpatterns = [
                      url(r'^__debug__/', include(debug_toolbar.urls)),
                  ] + urlpatterns
"""pudge URL Configuration

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
from pudge import settings
from pudge.views import *
from blog.views import *
# import blog.urls
# import demo.urls
from django.contrib.auth.decorators import login_required
from rest_framework.documentation import include_docs_urls


urlpatterns = [
    path('', index),                                        # 首页
    path('admin/', admin.site.urls),                        # 管理
    path('app', app, name='app'),                           # 应用
    path('blog/article', article_list, name='article_list'),
    path('blog/article/new', login_required(ArticleNewView.as_view(), login_url='/api-auth/login'), name='article_new'),
    path('blog/article/<uuid:article_id>', article_detail, name='article_detail'),
    path('blog/article/<uuid:article_id>/edit', login_required(ArticleEditView.as_view(), login_url='/api-auth/login'), name='article_edit'),

    # path('blog/todo', todo_list, name='todo_list'),
    # path('blog/article/new', login_required(ArticleNewView.as_view(), login_url='/api-auth/login'), name='article_new'),
    # path('blog/article/<uuid:article_id>', article_detail, name='article_detail'),
    # path('blog/article/<uuid:article_id>/edit', login_required(ArticleEditView.as_view(), login_url='/api-auth/login'), name='article_edit'),

    path('blog', include('blog.urls')),

    path('mdeditor/', include('mdeditor.urls')),
    path('api-auth/', include('rest_framework.urls')),
    # path('api-demo/', include(demo.urls.urlpatterns)),
    path('demo/', include('demo.urls')),

    # path('auth/', include('django.contrib.auth.urls')),  # 模板需要自己写
]

urlpatterns += [
    url("docs/", include_docs_urls(title="MY API DOCS")),
]

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
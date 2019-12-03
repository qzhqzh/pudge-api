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
import demo.urls
from django.urls import path, include
from django.contrib import admin
from django.conf.urls.static import static
from pudge import settings
from pudge.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('app.html', app),
    path('blog/index.html', blog),
    path('blog/article/<uuid:id>/detail.html', article_detail),
    path('mdeditor/', include('mdeditor.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api-demo/', include(demo.urls.urlpatterns))
]

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
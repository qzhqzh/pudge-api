from django.urls import path

from core.views import editor

test_urlpatterns = [
    path('editor', editor),
]

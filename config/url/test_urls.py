from django.urls import path

from core.views import test_demo

test_urlpatterns = [
    path('test', test_demo, name='home'),
]

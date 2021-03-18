from django.urls import path
from core.views import index, mylogin, mylogout
from kbms.views import editor


html_urlpatterns = [
    # 主页
    path('', index, name='home'),
    # 登陆
    path('login', mylogin, name='login'),
    # 登出
    path('logout', mylogout, name='logout'),

    # 编辑器
    path('editor', editor, name='editor'),
]

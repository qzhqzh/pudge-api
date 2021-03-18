from django.urls import path
from .views import index, mylogin, mylogout

urlpatterns = [
    # 主页
    path('', index, name='home'),
    # 登陆
    path('login', mylogin, name='login'),
    # 登出
    path('logout', mylogout, name='logout'),
]

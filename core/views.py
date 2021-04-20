from rest_framework.viewsets import ModelViewSet
from core.models import Attachment
from core.serializers import AttachmentSerializer

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from django.template.defaulttags import register

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import HttpResponse


class AttachmentViewSet(ModelViewSet):
    queryset = Attachment.objects.all()
    serializer_class = AttachmentSerializer


@register.filter
def get_range_start_with_1(value):
    return range(value)


def index(request):
    return render(request, 'index.html', {'page': 'Home'})


def mylogin(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        print(password)
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                # login 和 auth_login 函数会 send session id 到客户端
                return HttpResponseRedirect('/')
            else:
                HttpResponse('用户未激活')
        else:
            return HttpResponse('用户密码错误或者用户不存在')

        # print(username, password)
        # return redirect('/login')
    return render(request, 'login.html', {'page': 'Login'})


def mylogout(request):
    logout(request)
    return HttpResponseRedirect('/')

def test_demo(request):
    return render(request, 'index.html', {})
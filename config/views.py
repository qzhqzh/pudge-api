from django.shortcuts import render

from django.template.defaulttags import register

@register.filter
def get_range_start_with_1(value):
    return range(value)


def index(request):
    return render(request, 'index.html', {'page': 'Home'})

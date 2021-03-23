from django.shortcuts import render

def editor(request):
    return render(request, 'editor.html', {'page': 'Editor'})


def create_article(request):
    return render(request, 'kbms/create-article.html', {'page': 'Editor'})

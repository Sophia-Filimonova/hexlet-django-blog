# from django.shortcuts import render

# Create your views here.

from django.shortcuts import render


def index(request):
    title = 'article'
    return render(request, 'articles/index.html',
                  context = {'title': title})

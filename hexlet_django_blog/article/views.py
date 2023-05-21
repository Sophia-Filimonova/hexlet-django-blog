# from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.views import View

class IndexView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, Article!')


def index(request, tags, article_id):
    return HttpResponse(f'Статья номер {article_id}. Тег {tags}')

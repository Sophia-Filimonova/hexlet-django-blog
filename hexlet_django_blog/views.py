from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic.base import TemplateView


class IndexView(TemplateView):

    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['who'] = 'World'
        return context


def home_page(request):
    #return redirect(
    #    reverse('article', kwargs={'tags': 'python', 'article_id': 42}))
    return redirect(
        'article', tags='python', article_id=42)

def about(request):
    tags = ['обучение', 'программирование', 'python', 'oop']
    return render(
        request,
        'about.html',
        context={'tags': tags},
    )

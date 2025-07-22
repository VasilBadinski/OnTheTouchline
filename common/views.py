from django.views.generic import ListView
from articles.models import Article
from core.models import Leagues


class HomePage(ListView):
    model = Article
    template_name = 'index.html'
    context_object_name = "articles"

    def get_queryset(self):
        return Article.objects.all().order_by('-created_at')

class NewsPageView(ListView):
    model = Article
    template_name = 'news.html'
    context_object_name = 'articles'

    def get_queryset(self):
        return Article.objects.all().order_by('-created_at')

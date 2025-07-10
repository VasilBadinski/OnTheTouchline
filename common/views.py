from django.views.generic import ListView
from articles.models import Article


class HomePage(ListView):
    model = Article
    template_name = 'index.html'

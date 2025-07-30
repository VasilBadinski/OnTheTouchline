from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView
from articles.models import Article
from articles.forms import ArticleCreateForm, ArticleEditForm


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article/article_details.html'
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        article_name = self.kwargs.get('slug')
        article = get_object_or_404(Article, slug=article_name)
        context['article'] = article
        return context

class ArticleCreateView(CreateView):
    model = Article
    template_name = 'article/create_article.html'
    form_class = ArticleCreateForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.author = self.request.user.profiles
        return super().form_valid(form)

class ArticleEditView(UpdateView):
    model = Article
    form_class = ArticleEditForm
    template_name = 'article/edit_article.html'

    def get_success_url(self):
        return reverse_lazy(
            'article-detail',
            kwargs={'slug': self.object.slug}
        )

class ArticleDeleteView(DeleteView):
    model = Article
    context_object_name = 'article'
    template_name = 'article/article_delete.html'
    success_url = reverse_lazy('home')
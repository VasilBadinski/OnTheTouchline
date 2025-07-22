from django.urls import path, include

from articles.views import ArticleCreateView, ArticleDetailView, ArticleEditView, ArticleDeleteView

urlpatterns = [
    path('create/', ArticleCreateView.as_view(), name='article-create'),
    path('<slug:slug>/', include([
        path('', ArticleDetailView.as_view(), name='article-detail'),
        path('edit/', ArticleEditView.as_view(), name='article-edit'),
        path('delete/', ArticleDeleteView.as_view(), name='article-delete'),
    ])),
]
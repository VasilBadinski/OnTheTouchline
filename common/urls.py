from django.urls import path, include
from common import views
from common.views import NewsPageView

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('account/', include('accounts.urls')),
    path('new/', include('articles.urls')),
    path('news/', NewsPageView.as_view(), name='news'),
    path('', include('core.urls')),

]
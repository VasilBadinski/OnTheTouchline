from django.urls import path, include
from common import views
from common.views import NewsPageView, privacy_policy, terms_of_use, ContactMessageCreateView

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('account/', include('accounts.urls')),
    path('new/', include('articles.urls')),
    path('news/', NewsPageView.as_view(), name='news'),
    path('', include('core.urls')),
    path('quizes/', include('games.urls')),
    path('privacy-policy/', privacy_policy, name='privacy_policy'),
    path('terms-of-use/', terms_of_use, name='terms_of_use'),
    path('contact_us/', ContactMessageCreateView.as_view(), name='contact-us'),
]
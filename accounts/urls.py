from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include

from accounts.views import ProfileRegisterView, ProfileDetailsView

urlpatterns = [
    path('', include([
        path('register/', ProfileRegisterView.as_view(), name='register'),
        path('login/', LoginView.as_view(template_name='login.html'), name='login'),
        path('logout/', LogoutView.as_view(), name='logout'),
        path('profile/<int:pk>/', include([
            path('', ProfileDetailsView.as_view(), name='detail_profile'),
        ]))
    ]))
]

from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from accounts.views import ProfileRegisterView, ProfileDetailsView, ProfileDeleteView, ProfileEditView, \
    ProfileCreateView

urlpatterns = [
    path('', include([
        path('register/', include([
            path('', ProfileRegisterView.as_view(), name='register'),
            path('profile-register/', ProfileCreateView.as_view(), name='register-profile')
        ])),
        path('logout/', LogoutView.as_view(), name='logout'),
        path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
        path('profile/<int:pk>/', include([
            path('', ProfileDetailsView.as_view(), name='detail-profile'),
            path('delete/', ProfileDeleteView.as_view(), name='delete'),
            path('edit/', ProfileEditView.as_view(), name='edit')
        ]))
    ]))
]

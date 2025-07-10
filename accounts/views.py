from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from accounts.forms import AppUserCreationForm
from accounts.models import Profile

UserModel = get_user_model()

class ProfileRegisterView(CreateView):
    model = UserModel
    form_class = AppUserCreationForm
    template_name = 'register_profile.html'
    success_url = reverse_lazy('login')

class ProfileDetailsView(DetailView):
    model = UserModel
    template_name = 'profile_details.html'
    context_object_name = 'profile'
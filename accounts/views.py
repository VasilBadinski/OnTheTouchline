from django.contrib.auth import get_user_model, login
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView
from accounts.forms import AppUserCreationForm, ProfileEditForm, ProfileCreateForm
from accounts.models import Profile

UserModel = get_user_model()

class ProfileRegisterView(CreateView):
    model = UserModel
    form_class = AppUserCreationForm
    template_name = 'register_account.html'
    success_url = reverse_lazy('register-profile')

    def form_valid(self, form):
        response = super().form_valid(form)
        Profile.objects.create(user=self.object)
        login(self.request, self.object)
        return response

class ProfileCreateView(CreateView):
    model = Profile
    form_class = ProfileCreateForm
    template_name = 'register_profile.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ProfileDetailsView(DetailView):
    model = Profile
    template_name = 'profile_details.html'
    context_object_name = 'profile'

class ProfileDeleteView(DeleteView):
    model = UserModel
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        return self.request.user

    def delete(self, request, *args, **kwargs):
        user = self.get_object()
        user.delete()
        return redirect(self.get_success_url())

class ProfileEditView(UpdateView):
    model = Profile
    form_class = ProfileEditForm
    template_name = 'edit_profile.html'

    def get_object(self, queryset = None):
        return self.request.user.profiles

    def get_success_url(self):
        return reverse_lazy(
            'detail-profile',
            kwargs={'pk': self.object.pk}
        )
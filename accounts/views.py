from django.contrib.auth import get_user_model, logout
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView
from accounts.forms import AppUserCreationForm, ProfileEditForm, ProfileCreateForm
from accounts.models import Profile

UserModel = get_user_model()

class ProfileRegisterView(CreateView):
    model = UserModel
    form_class = AppUserCreationForm
    template_name = 'accounts/register_account.html'
    success_url = reverse_lazy('register-profile')

    def form_valid(self, form):
        response = super().form_valid(form)
        self.request.session['new_user_id'] = self.object.pk
        return response

class ProfileCreateView(CreateView):
    model = Profile
    form_class = ProfileCreateForm
    template_name = 'accounts/register_profile.html'
    success_url = reverse_lazy('login')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated or 'new_user_id' not in request.session:
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        user_id = self.request.session.pop('new_user_id', None)
        if not user_id:
            return redirect('login')

        user = UserModel.objects.get(pk=user_id)
        form.instance.user = user
        return super().form_valid(form)

class ProfileDetailsView(DetailView):
    model = Profile
    template_name = 'accounts/profile_details.html'
    context_object_name = 'profile'

class ProfileDeleteView(DeleteView):
    model = UserModel
    template_name = 'accounts/profile_delete.html'
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        return self.request.user

    def delete(self, request, *args, **kwargs):
        logout(request)
        return super().delete(request, *args, **kwargs)

class ProfileEditView(UpdateView):
    model = Profile
    form_class = ProfileEditForm
    template_name = 'accounts/edit_profile.html'

    def get_object(self, queryset = None):
        return self.request.user.profiles

    def get_success_url(self):
        return reverse_lazy(
            'detail-profile',
            kwargs={'pk': self.object.pk}
        )
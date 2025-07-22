from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm
from accounts.models import Profile
from django import forms

UserModel = get_user_model()

class AppUserCreationForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ['email']

class AppUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = UserModel

class ProfileCreateForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['username', 'date_of_birth', 'profile_picture']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }

class ProfileEditForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['username', 'date_of_birth', 'profile_picture']
        labels = {
            'username': 'Username:',
            'date_of_birth': 'Date of birth:',
            'profile_picture': 'Profile picture:'
        }
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }
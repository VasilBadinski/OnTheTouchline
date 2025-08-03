from django import forms
from django.forms import Textarea
from .models import Quiz


class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ['title', 'description', 'eng_title', 'image']

        widgets = {
            'description': Textarea(),
        }

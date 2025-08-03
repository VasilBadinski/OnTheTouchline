from django import forms
from django.forms import Textarea
from common.models import ContactMessage


class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['email', 'message']
        widgets = {
            'message': Textarea(),
        }

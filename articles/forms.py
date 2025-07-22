from django.forms import ModelForm
from django.forms.widgets import Textarea
from articles.models import Article


class ArticleCreateForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'description', 'imageURL']
        widgets = {
            'description': Textarea(),
        }

class ArticleEditForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'description', 'imageURL']
        labels = {
            'title': 'Title:',
            'description': 'Description:',
            'imageURL': 'Image:'
        }
        widgets = {
            'description': Textarea(),
        }
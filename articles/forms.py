from django.forms import ModelForm
from django.forms.widgets import Textarea
from articles.models import Article

class ArticleCreateForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'description', 'imageURL', 'league', 'club', 'player']
        widgets = {
            'description': Textarea(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['league'].empty_label = "Избери лига"
        self.fields['club'].empty_label = "Избери отбор"
        self.fields['player'].empty_label = "Избери играч"


class ArticleEditForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'description', 'imageURL', 'league', 'club', 'player']
        labels = {
            'title': 'Title:',
            'description': 'Description:',
            'imageURL': 'Image:',
            'league': 'League:',
            'club': 'Club:',
            'player': 'Player:',
        }
        widgets = {
            'description': Textarea(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['league'].empty_label = "Избери лига"
        self.fields['club'].empty_label = "Избери отбор"
        self.fields['player'].empty_label = "Избери играч"

from django.forms.models import ModelForm
from core.models import Leagues, Clubs, Player


class LeagueAddForm(ModelForm):
    class Meta:
        model = Leagues
        fields = ['name', 'logo', 'eng_name']


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['eng_name'].initial = ''

class ClubAddForm(ModelForm):
    class Meta:
        model = Clubs
        fields = ['name', 'logo', 'eng_name', 'league']


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['eng_name'].initial = ''
        self.fields['league'].empty_label = "Избери лига"

class PlayerAddForm(ModelForm):
    class Meta:
        model = Player
        fields = ['name', 'photo', 'eng_name', 'club']


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['eng_name'].initial = ''
        self.fields['club'].empty_label = "Избери клуб"
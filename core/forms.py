from django import forms
from django.forms.models import ModelForm, ModelChoiceField
from core.models import Leagues, Clubs, Player, Matches


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
        fields = ['name', 'position', 'photo', 'number', 'eng_name', 'club', 'date_of_birth', 'height']

        widgets = {
            'date_of_birth': forms.DateTimeInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['eng_name'].initial = ''
        self.fields['club'].empty_label = "Избери клуб"


class MatchCreateForm(forms.ModelForm):
    class Meta:
        model = Matches
        fields = ['league', 'home_team', 'away_team', 'date']
        widgets = {
            'date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'league': forms.Select(attrs={'id': 'id_league'}),
            'home_team': forms.Select(attrs={'id': 'id_home_team'}),
            'away_team': forms.Select(attrs={'id': 'id_away_team'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['league'].empty_label = "Избери лига"
        self.fields['home_team'].empty_label = "Избери домакин"
        self.fields['away_team'].empty_label = "Избери гост"

        if self.data.get('league'):
            try:
                league_id = int(self.data.get('league'))
                self.fields['home_team'].queryset = Clubs.objects.filter(league_id=league_id)
                self.fields['away_team'].queryset = Clubs.objects.filter(league_id=league_id)
            except (ValueError, TypeError):
                self.fields['home_team'].queryset = Clubs.objects.none()
                self.fields['away_team'].queryset = Clubs.objects.none()


class LeagueEditForm(forms.ModelForm):
    class Meta:
        model = Leagues
        fields = ['name', 'logo', 'eng_name']
        labels = {
            'name': 'Name:',
            'logo': 'Logo:',
            'eng_name': 'English name:',
        }

class ClubEditForm(forms.ModelForm):
    class Meta:
        model = Clubs
        fields = ['name', 'logo', 'eng_name', 'league']
        labels = {
            'name': 'Name:',
            'logo': 'Logo:',
            'eng_name': 'English name:',
            'league': 'League:',
        }

class MatchEditForm(forms.ModelForm):
    class Meta:
        model = Matches
        fields = ['league', 'home_team', 'away_team', 'date']
        labels = {
            'league': 'League:',
            'home_team': 'Home team:',
            'away_team': 'Away team:',
            'date': 'Date:',
        }

        widgets = {
            'date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class PlayerEditForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['name', 'position', 'photo', 'number', 'eng_name', 'club', 'date_of_birth', 'height']
        labels = {
            'name': 'Name:',
            'position': 'Position:',
            'photo': 'Photo:',
            'number': 'Number:',
            'eng_name': 'English name:',
            'club': 'Club:',
            'date_of_birth': 'Date of birth',
            'height': 'Height',
        }

        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }
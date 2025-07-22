from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from core.forms import LeagueAddForm, ClubAddForm, PlayerAddForm
from core.models import Leagues, Clubs, Player


class LeaguePageView(ListView):
    model = Leagues
    template_name = 'league.html'
    context_object_name = 'leagues'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        league_slug = self.kwargs.get('slug')
        league = get_object_or_404(Leagues, slug=league_slug)
        context['league'] = league
        return context

class LeagueAddView(CreateView):
    model = Leagues
    template_name = 'add_league.html'
    form_class = LeagueAddForm
    success_url = reverse_lazy('home')

class ClubsAddCView(CreateView):
    model = Clubs
    template_name = 'add_club.html'
    form_class = ClubAddForm
    success_url = reverse_lazy('home')

class PlayersAddView(CreateView):
    model = Player
    template_name = 'add_player.html'
    form_class = PlayerAddForm
    success_url = reverse_lazy('home')

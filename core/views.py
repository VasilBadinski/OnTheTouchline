from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from articles.models import Article
from core.forms import LeagueAddForm, ClubAddForm, PlayerAddForm, MatchCreateForm, LeagueEditForm, ClubEditForm
from core.models import Leagues, Clubs, Player, Matches


class LeaguePageView(DetailView):
    model = Leagues
    template_name = 'league.html'
    context_object_name = 'league'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        league = self.object

        articles = Article.objects.filter(league=league).order_by('-created_at')
        context['articles'] = articles

        clubs = list(league.clubs.all())
        standings = sorted(
            clubs,
            key=lambda club: (club.points, club.goal_difference, club.s_goals),
            reverse=True
        )
        context['standings'] = standings

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


class MatchCreateView(CreateView):
    model = Matches
    form_class = MatchCreateForm
    template_name = 'add_match.html'
    success_url = reverse_lazy('home')


class ClubPageView(DetailView):
    model = Clubs
    template_name = 'team.html'
    context_object_name = 'club'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        club = self.get_object()
        context['articles'] = Article.objects.filter(club=club).order_by('-created_at')

        position_labels = {
            'GK': 'Вратари',
            'DF': 'Защитници',
            'MF': 'Халфове',
            'AT': 'Нападатели',
        }

        players_by_position = {}
        for position, label in position_labels.items():
            players_by_position[position] = {
                'label': label,
                'players': club.players.filter(position=position)
            }

        context['players_by_position'] = players_by_position
        return context


class LeagueEditView(UpdateView):
    model = Leagues
    form_class = LeagueEditForm
    context_object_name = 'league'
    template_name = 'edit_league.html'

    def get_success_url(self):
        return reverse_lazy(
            'league',
            kwargs={'slug': self.object.slug}
        )

class ClubEditView(UpdateView):
    model = Clubs
    form_class = ClubEditForm
    context_object_name = 'club'
    template_name = 'edit_club.html'

    def get_success_url(self):
        return reverse_lazy(
            'club',
            kwargs={'slug': self.object.slug}
        )
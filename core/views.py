from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView
from articles.models import Article
from common.mixins import ClubContextMixin
from core.choices import PlayerPositionChoices
from core.forms import LeagueAddForm, ClubAddForm, PlayerAddForm, MatchCreateForm, LeagueEditForm, ClubEditForm, \
    MatchEditForm, PlayerEditForm
from core.models import Leagues, Clubs, Player, Matches


class LeaguePageView(DetailView):
    model = Leagues
    template_name = 'core/league/league.html'
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
    template_name = 'core/league/add_league.html'
    form_class = LeagueAddForm
    success_url = reverse_lazy('home')

class ClubsAddCView(CreateView):
    model = Clubs
    template_name = 'core/club/add_club.html'
    form_class = ClubAddForm
    success_url = reverse_lazy('home')

class PlayersAddView(CreateView):
    model = Player
    template_name = 'core/player/add_player.html'
    form_class = PlayerAddForm
    success_url = reverse_lazy('home')


class MatchCreateView(CreateView):
    model = Matches
    form_class = MatchCreateForm
    template_name = 'core/match/add_match.html'
    success_url = reverse_lazy('home')


class ClubPageView(DetailView):
    model = Clubs
    template_name = 'core/club/team.html'
    context_object_name = 'club'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        club = self.get_object()
        context['articles'] = Article.objects.filter(club=club).order_by('-created_at')
        return context


class LeagueEditView(UpdateView):
    model = Leagues
    form_class = LeagueEditForm
    context_object_name = 'league'
    template_name = 'core/league/edit_league.html'

    def get_success_url(self):
        return reverse_lazy(
            'league',
            kwargs={'slug': self.object.slug}
        )

class ClubEditView(UpdateView):
    model = Clubs
    form_class = ClubEditForm
    context_object_name = 'club'
    template_name = 'core/club/edit_club.html'

    def get_success_url(self):
        return reverse_lazy(
            'club',
            kwargs={'slug': self.object.slug}
        )

class OverviewView(ClubContextMixin, DetailView):
    model = Clubs
    context_object_name = 'club'
    template_name = 'core/club/overview.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        club = self.get_club()

        context['upcoming_matches'] = self.get_upcoming_matches(club)
        context['articles'] = self.get_articles(club)[:2]
        context['stadium'] = getattr(club, 'club', None)
        return context


class ClubMatchView(ClubContextMixin, DetailView):
    model = Clubs
    context_object_name = 'club'
    template_name = 'core/club/matches.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        club = self.get_club()
        context['upcoming_matches'] = self.get_upcoming_matches(club)
        return context


class SquadView(ClubContextMixin, DetailView):
    model = Clubs
    context_object_name = 'club'
    template_name = 'core/club/players.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        club = self.get_club()

        context['goalkeepers'] = club.players.filter(position=PlayerPositionChoices.GOALKEEPER)
        context['defenders'] = club.players.filter(position=PlayerPositionChoices.DEFENDER)
        context['midfielders'] = club.players.filter(position=PlayerPositionChoices.MIDFIELDER)
        context['attackers'] = club.players.filter(position=PlayerPositionChoices.ATTACKER)

        return context


class ClubNewsView(ClubContextMixin, DetailView):
    model = Clubs
    context_object_name = 'club'
    template_name = 'core/club/club_news.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        club = self.get_club()

        context['articles'] = self.get_articles(club)
        return context


class ClubDeleteView(DeleteView):
    model = Clubs
    context_object_name = 'club'
    template_name = 'core/club/club_delete.html'


    def get_success_url(self):
        club = self.get_object()
        league_slug = club.league.slug
        return reverse('league', kwargs={'slug': league_slug})


class LeagueDeleteView(DeleteView):
    model = Leagues
    context_object_name = 'league'
    template_name = 'core/league/league_delete.html'
    success_url = reverse_lazy('home')

class MatchView(DetailView):
    model = Matches
    context_object_name = 'match'
    template_name = 'core/match/match_page.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        match = self.object
        league = match.league

        clubs = list(league.clubs.all())
        standings = sorted(
            clubs,
            key=lambda club: (club.points, club.goal_difference, club.s_goals),
            reverse=True
        )
        context['standings'] = standings
        return context

class MatchEditView(UpdateView):
    model = Matches
    form_class = MatchEditForm
    context_object_name = 'match'
    template_name = 'core/match/edit_match.html'

    def get_success_url(self):
        return reverse_lazy(
            'match',
            kwargs={'slug': self.object.slug}
        )


class MatchDeleteView(DeleteView):
    model = Matches
    context_object_name = 'match'
    template_name = 'core/match/delete_match.html'
    success_url = reverse_lazy('home')


class PlayerView(DetailView):
    model = Player
    context_object_name = 'player'
    template_name = 'core/player/player.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        player = self.get_object()

        context['articles'] = Article.objects.filter(player=player).order_by('-created_at')
        return context


class PlayerDeleteView(DeleteView):
    model = Player
    context_object_name = 'player'
    template_name = 'core/player/delete_player.html'
    success_url = reverse_lazy('home')


class PlayerEditView(UpdateView):
    model = Player
    form_class = PlayerEditForm
    context_object_name = 'player'
    template_name = 'core/player/edit_player.html'

    def get_success_url(self):
        return reverse_lazy(
            'player',
            kwargs={'slug': self.object.slug}
        )
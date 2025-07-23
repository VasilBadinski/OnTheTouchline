from django.http import JsonResponse
from django.views.generic import ListView
from articles.models import Article
from core.models import Clubs, Player


class HomePage(ListView):
    model = Article
    template_name = 'index.html'
    context_object_name = "articles"

    def get_queryset(self):
        return Article.objects.all().order_by('-created_at')

class NewsPageView(ListView):
    model = Article
    template_name = 'news.html'
    context_object_name = 'articles'

    def get_queryset(self):
        return Article.objects.all().order_by('-created_at')


def clubs_by_league(request):
    league_id = request.GET.get('league_id')
    if league_id:
        clubs = Clubs.objects.filter(league_id=league_id).order_by('eng_name')
    else:
        clubs = Clubs.objects.none()
    clubs_list = list(clubs.values('id', 'eng_name'))
    return JsonResponse({'clubs': clubs_list})


def players_by_club(request):
    club_id = request.GET.get('club_id')
    if club_id:
        players = Player.objects.filter(club_id=club_id).order_by('eng_name')
    else:
        players = Player.objects.none()
    players_list = list(players.values('id', 'eng_name'))
    return JsonResponse({'players': players_list})

from asgiref.sync import sync_to_async
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


async def clubs_by_league(request):
    league_id = request.GET.get('league_id')
    if league_id:
        clubs = await sync_to_async(list)(
            Clubs.objects.filter(league_id=league_id).order_by('eng_name').values('id', 'eng_name')
        )
    else:
        clubs = []
    return JsonResponse({'clubs': clubs})


async def players_by_club(request):
    club_id = request.GET.get('club_id')
    if club_id:
        players = await sync_to_async(list)(
            Player.objects.filter(club_id=club_id).order_by('eng_name').values('id', 'eng_name')
        )
    else:
        players = []
    return JsonResponse({'players': players})

from collections import defaultdict
from asgiref.sync import sync_to_async
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView
from articles.models import Article
from common.forms import ContactMessageForm
from core.models import Clubs, Player, Matches


class HomePage(ListView):
    model = Article
    template_name = 'common/index.html'
    context_object_name = "articles"

    def get_queryset(self):
        return Article.objects.all().order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        matches = Matches.objects.select_related('home_team', 'away_team', 'league').order_by('date')

        grouped = defaultdict(list)
        for match in matches:
            if len(grouped[match.league.name]) < 5:
                grouped[match.league.name].append(match)

        context['grouped_matches'] = dict(grouped)
        return context


class ContactMessageCreateView(FormView):
    template_name = 'common/contact_us.html'
    form_class = ContactMessageForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


def privacy_policy(request):
    return render(request, 'common/privacy_policy.html')

def terms_of_use(request):
    return render(request, 'common/terms_of_service.html')


class NewsPageView(ListView):
    model = Article
    template_name = 'article/news.html'
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

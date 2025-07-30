from django.urls import path, include
from core.views import LeaguePageView, LeagueAddView, ClubsAddCView, PlayersAddView, MatchCreateView, ClubPageView, \
    LeagueEditView, ClubEditView, OverviewView, ClubMatchView, ClubDeleteView, LeagueDeleteView, SquadView, \
    ClubNewsView, MatchView, MatchEditView, MatchDeleteView, PlayerEditView, PlayerDeleteView, PlayerView

urlpatterns = [
    path('leagues/', include([
        path('add', LeagueAddView.as_view(), name='add-league'),
        path('<slug:slug>/', include([
            path('', LeaguePageView.as_view(), name='league'),
            path('edit/', LeagueEditView.as_view(), name='edit-league'),
            path('delete/', LeagueDeleteView.as_view(), name='delete-league'),
        ])),
    ])),
    path('clubs/', include([
        path('add/', ClubsAddCView.as_view(), name='add-club'),
        path('<slug:slug>/', include([
            path('', ClubPageView.as_view(), name='club'),
            path('edit/', ClubEditView.as_view(), name='edit-club'),
            path('delete/', ClubDeleteView.as_view(), name='delete-club'),
            path('overview/', OverviewView.as_view(), name='overview'),
            path('matches/', ClubMatchView.as_view(), name='matches'),
            path('squad/', SquadView.as_view(), name='squad'),
            path('news/', ClubNewsView.as_view(), name='club-news'),
        ]))
    ])),
    path('players/', include([
        path('add/', PlayersAddView.as_view(), name='add-player'),
        path('<slug:slug>/', include([
            path('', PlayerView.as_view(), name='player'),
            path('edit/', PlayerEditView.as_view(), name='edit-player'),
            path('delete/', PlayerDeleteView.as_view(), name='delete-player')
        ]))
    ])),
    path('match/', include([
        path('add/', MatchCreateView.as_view(), name='add-matches'),
        path('<slug:slug>/', include([
            path('', MatchView.as_view(), name='match'),
            path('edit/', MatchEditView.as_view(), name='edit-match'),
            path('delete/', MatchDeleteView.as_view(), name='delete-match')
        ])),
    ]))
]
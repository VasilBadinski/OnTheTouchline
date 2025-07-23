from django.urls import path, include
from core.views import LeaguePageView, LeagueAddView, ClubsAddCView, PlayersAddView, MatchCreateView, ClubPageView, \
    LeagueEditView, ClubEditView

urlpatterns = [
    path('leagues/', include([
        path('add', LeagueAddView.as_view(), name='add-league'),
        path('<slug:slug>/', include([
            path('', LeaguePageView.as_view(), name='league'),
            path('edit/', LeagueEditView.as_view(), name='edit-league'),
        ])),
    ])),
    path('clubs/', include([
        path('add/', ClubsAddCView.as_view(), name='add-club'),
        path('<slug:slug>/', include([
            path('', ClubPageView.as_view(), name='club'),
            path('edit/', ClubEditView.as_view(), name='edit-club')\
        ]))
    ])),
    path('players/', include([
        path('add/', PlayersAddView.as_view(), name='add-player'),
    ])),
    path('matches/', MatchCreateView.as_view(), name='add-matches')
]
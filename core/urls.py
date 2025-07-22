from django.urls import path, include
from core.views import LeaguePageView, LeagueAddView, ClubsAddCView, PlayersAddView

urlpatterns = [
    path('leagues/', include([
        path('add', LeagueAddView.as_view(), name='add-league'),
        path('<slug:slug>/', LeaguePageView.as_view(), name='league'),
    ])),
    path('clubs/', include([
        path('add/', ClubsAddCView.as_view(), name='add-club'),
    ])),
    path('players/', include([
        path('add/', PlayersAddView.as_view(), name='add-player'),
    ])),
]

from django.contrib import admin
from django.urls import path, include
from common import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ajax/get-clubs/', views.clubs_by_league, name='ajax_get_clubs'),
    path('ajax/get-players/', views.players_by_club, name='ajax_get_players'),
    path('', include('common.urls')),
]

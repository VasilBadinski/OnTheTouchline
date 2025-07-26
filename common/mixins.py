from django.utils import timezone
from django.db import models

from articles.models import Article
from core.models import Matches


class ClubContextMixin:
    def get_club(self):
        return self.get_object()

    def get_upcoming_matches(self, club):
        now = timezone.now()
        return Matches.objects.filter(
            date__gte=now
        ).filter(
            models.Q(home_team=club) | models.Q(away_team=club)
        ).order_by('date')[:5]

    def get_articles(self, club):
        return Article.objects.filter(club=club).order_by('-created_at')

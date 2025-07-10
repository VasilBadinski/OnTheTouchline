from django.db import models

class Leagues(models.Model):
    name = models.CharField(max_length=100)
    logo = models.URLField()

class Clubs(models.Model):
    name = models.CharField(max_length=100)
    logo = models.URLField()
    league = models.ForeignKey(Leagues, on_delete=models.CASCADE, related_name='clubs')

class Player(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=50)
    photo = models.URLField()
    club = models.ForeignKey(Clubs, on_delete=models.CASCADE, related_name='players')

class Matches(models.Model):
    home_team = models.ForeignKey(Clubs, on_delete=models.CASCADE, related_name='home_matches')
    away_team = models.ForeignKey(Clubs, on_delete=models.CASCADE, related_name='away_matches')
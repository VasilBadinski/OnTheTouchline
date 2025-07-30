from datetime import date
from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from core.choices import PlayerPositionChoices


class Leagues(models.Model):
    name = models.CharField(max_length=100)
    logo = models.URLField()
    eng_name = models.CharField(max_length=100, default='Unknown')
    slug = models.SlugField(unique=True, null=True)

    class Meta:
        ordering = ['pk']

    def __str__(self):
        return self.eng_name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.eng_name)
        super().save(*args, **kwargs)


class Clubs(models.Model):
    name = models.CharField(max_length=100)
    logo = models.URLField()
    eng_name = models.CharField(max_length=100, default='Unknown')
    slug = models.SlugField(unique=True, null=True)
    league = models.ForeignKey(Leagues, on_delete=models.CASCADE, related_name='clubs', null=True)
    points = models.PositiveIntegerField(
        default=0
    )
    goals = models.PositiveIntegerField(
        default=0
    )

    played_games = models.PositiveIntegerField(
        default=0
    )

    s_goals = models.PositiveIntegerField(
        default=0
    )

    c_goals = models.PositiveIntegerField(
        default=0
    )

    @property
    def goal_difference(self):
        return self.s_goals - self.c_goals


    def __str__(self):
        return self.eng_name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.eng_name)
        super().save(*args, **kwargs)



class Player(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=50, choices=PlayerPositionChoices.choices)
    photo = models.URLField()
    number = models.PositiveIntegerField(default=0)
    eng_name = models.CharField(max_length=100, default='Unknown')
    slug = models.SlugField(unique=True, null=True)
    club = models.ForeignKey(Clubs, on_delete=models.CASCADE, related_name='players')
    date_of_birth = models.DateField(default=date(2000, 1, 1))
    height = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.eng_name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.eng_name)
        super().save(*args, **kwargs)


class Matches(models.Model):
    league = models.ForeignKey(
        Leagues,
        on_delete=models.CASCADE,
        related_name='league',
        null=True)

    home_team = models.ForeignKey(
        Clubs,
        on_delete=models.CASCADE,
        related_name='home_matches'
    )

    away_team = models.ForeignKey(
        Clubs,
        on_delete=models.CASCADE,
        related_name='away_matches'
    )

    date = models.DateTimeField(
        default=timezone.now
    )
    slug = models.SlugField(unique=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f'{self.home_team.eng_name} {self.away_team.eng_name}')
        super().save(*args, **kwargs)

class PlayerStats(models.Model):
    player = models.OneToOneField(
        Player,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='players'
    )

    played_games = models.PositiveIntegerField(
        default=0
    )

    goals = models.PositiveIntegerField(
        default=0
    )

    assists = models.PositiveIntegerField(
        default=0
    )

    yellow_cards = models.PositiveIntegerField(
        default=0
    )

    red_cards = models.PositiveIntegerField(
        default=0
    )

    minutes_played = models.PositiveIntegerField(
        default=0
    )

class Stadium(models.Model):
    name = models.CharField(max_length=100, null=True)
    club = models.OneToOneField(Clubs, on_delete=models.CASCADE, primary_key=True, related_name='club')
    capacity = models.PositiveIntegerField()
    opened = models.PositiveIntegerField()
    city = models.CharField(max_length=50)
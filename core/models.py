from django.db import models
from django.utils import timezone
from django.utils.text import slugify


class Leagues(models.Model):
    name = models.CharField(max_length=100)
    logo = models.URLField()
    eng_name = models.CharField(max_length=100, default='Unknown')
    slug = models.SlugField(unique=True, blank=True)

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
    slug = models.SlugField(unique=True, blank=True)
    league = models.ForeignKey(Leagues, on_delete=models.CASCADE, related_name='clubs')

    def __str__(self):
        return self.eng_name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.eng_name)
        super().save(*args, **kwargs)

class Player(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=50)
    photo = models.URLField()
    eng_name = models.CharField(max_length=100, default='Unknown')
    slug = models.SlugField(unique=True, blank=True)
    club = models.ForeignKey(Clubs, on_delete=models.CASCADE, related_name='players')

    def __str__(self):
        return self.eng_name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.eng_name)
        super().save(*args, **kwargs)

class Matches(models.Model):
    home_team = models.ForeignKey(Clubs, on_delete=models.CASCADE, related_name='home_matches')
    away_team = models.ForeignKey(Clubs, on_delete=models.CASCADE, related_name='away_matches')
    date = models.DateTimeField(default=timezone.now)
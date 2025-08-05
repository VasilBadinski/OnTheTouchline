from rest_framework import serializers
from core.models import Player, Leagues, Clubs


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['id', 'name', 'slug', 'photo']

class LeagueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leagues
        fields = ['id', 'name', 'slug', 'logo']

class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clubs
        fields = ['id', 'name', 'slug', 'logo']
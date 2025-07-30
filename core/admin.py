from django.contrib import admin
from core.models import Leagues, Clubs, Player, Matches, PlayerStats, Stadium


@admin.register(Leagues)
class LeagueAdmin(admin.ModelAdmin):
    list_display = ("eng_name", "name", "slug")
    search_fields = ("eng_name", "name")
    ordering = ("eng_name",)
    readonly_fields = ("slug",)


@admin.register(Clubs)
class ClubAdmin(admin.ModelAdmin):
    list_display = ("eng_name", "league", "points", "played_games", "goal_difference")
    list_filter = ("league",)
    search_fields = ("eng_name", "name")
    ordering = ("-points",)
    readonly_fields = ("slug",)

    @admin.display(description="Goal Difference")
    def goal_difference(self, obj):
        return obj.goal_difference


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ("eng_name", "club", "position", "number", "date_of_birth", "height")
    list_filter = ("position", "club")
    search_fields = ("eng_name", "name")
    ordering = ("club", "number")
    readonly_fields = ("slug",)


@admin.register(Matches)
class MatchAdmin(admin.ModelAdmin):
    list_display = ("league", "home_team", "away_team", "date")
    list_filter = ("league", "home_team", "away_team")
    search_fields = ("home_team__eng_name", "away_team__eng_name")
    ordering = ("-date",)
    readonly_fields = ("slug",)


@admin.register(PlayerStats)
class PlayerStatsAdmin(admin.ModelAdmin):
    list_display = ("player", "played_games", "goals", "assists", "minutes_played")
    list_filter = ("player__club",)
    search_fields = ("player__eng_name",)
    ordering = ("-goals",)


@admin.register(Stadium)
class StadiumAdmin(admin.ModelAdmin):
    list_display = ("name", "club", "capacity", "opened", "city")
    search_fields = ("name", "city", "club__eng_name")
    ordering = ("-capacity",)

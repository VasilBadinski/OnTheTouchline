from django.contrib import admin
from articles.models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "published", "created_at", "league", "club")
    list_filter = ("published", "created_at", "league", "club")
    search_fields = ("title", "description", "author__user__email")
    ordering = ("-created_at", "title")
    readonly_fields = ("created_at", "updated_at", "slug")
    fieldsets = (
        (None, {
            "fields": ("title", "description", "imageURL", "author")
        }
         ),
        (
            "Relations", {
            "fields": ("league", "club", "player")
        }),
        (
            "Publishing Info", {
            "fields": ("published", "slug")
        }),
        (
            "Timestamps", {
            "fields": ("created_at", "updated_at")
        }),
    )

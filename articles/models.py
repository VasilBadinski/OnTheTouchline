from django.core.validators import MinLengthValidator
from django.db import models
from django.utils.text import slugify
from accounts.models import Profile
from articles.validators import ArticleValidator
from core.models import Leagues, Player, Clubs


class Article(models.Model):
    title = models.CharField(
        max_length=150,
        validators=[
            MinLengthValidator(10),
            ArticleValidator
        ]
    )

    description = models.TextField(
        validators=[
            MinLengthValidator(30),
            ArticleValidator
        ]
    )

    imageURL = models.URLField()

    author = models.ForeignKey(
        Profile,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='article'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    published = models.BooleanField(default=False)

    slug = models.SlugField(
        max_length=150,
        unique=True,
        editable=False
    )

    league = models.ForeignKey(
        Leagues,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    club = models.ForeignKey(
        Clubs,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    player = models.ForeignKey(
        Player,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def save(self, *args, **kwargs):
        base_slug = slugify(self.title)
        slug = base_slug
        num = 1

        while Article.objects.filter(slug=slug).exclude(pk=self.pk).exists():
            slug = f"{base_slug}-{num}"
            num += 1

        self.slug = slug
        super().save(*args, **kwargs)
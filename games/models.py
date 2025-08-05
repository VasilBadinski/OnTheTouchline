from django.db import models
from django.utils.text import slugify
from accounts.models import Profile


class Quiz(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    published = models.BooleanField(default=False)
    eng_title = models.CharField(max_length=255, blank=True)
    image = models.URLField(null=True)
    slug = models.SlugField(max_length=150, unique=True, editable=False)

    def save(self, *args, **kwargs):
        base_slug = slugify(self.eng_title)
        slug = base_slug
        num = 1

        while Quiz.objects.filter(slug=slug).exclude(pk=self.pk).exists():
            slug = f"{base_slug}-{num}"
            num += 1

        self.slug = slug
        super().save(*args, **kwargs)


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, related_name='questions', on_delete=models.CASCADE)
    text = models.TextField()
    option_a = models.CharField(max_length=255)
    option_b = models.CharField(max_length=255)
    option_c = models.CharField(max_length=255)
    option_d = models.CharField(max_length=255)

    CORRECT_CHOICES = [
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
    ]
    correct_answer = models.CharField(max_length=1, choices=CORRECT_CHOICES)


class QuizAttempt(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    score = models.FloatField()
    time_completion = models.DateTimeField(null=True)

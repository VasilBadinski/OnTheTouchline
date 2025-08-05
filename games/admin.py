from django.contrib import admin
from games.models import Quiz, Question, QuizAttempt


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    pass

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    pass

@admin.register(QuizAttempt)
class QuizAttemptAdmin(admin.ModelAdmin):
    pass
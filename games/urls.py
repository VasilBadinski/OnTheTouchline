from django.urls import path, include
from games.views import AddQuizView, AddQuestionsView, QuizesView, GamesView, QuizesDetailView, QuizAnswersView

urlpatterns = [
    path('create/', include([
        path('', AddQuizView.as_view(), name='add-quiz'),
        path('add_question/<int:quiz_id>/<int:count>/', AddQuestionsView.as_view(), name='add-questions')])),
    path('games/', include([
        path('', GamesView.as_view(), name='games'),
        path('quizzes/', QuizesView.as_view(), name='quizes'),
        path('<slug:slug>/', include([
            path('', QuizesDetailView.as_view(), name='quiz'),
            path('answers/', QuizAnswersView.as_view(), name='quiz-answers')
        ]))
    ])),
]
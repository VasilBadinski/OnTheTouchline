from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.utils.timezone import now
from django.views import View
from django.views.generic import CreateView, TemplateView, ListView, DetailView
from django.shortcuts import redirect, get_object_or_404, render
from django.urls import reverse
from .models import Quiz, Question, QuizAttempt
from .forms import QuizForm


class GamesView(TemplateView):
    template_name = 'games/all_games.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['quizzes'] = Quiz.objects.all()
        # context['games'] = Game.objects.all()
        return context


class AddQuizView(CreateView):
    model = Quiz
    form_class = QuizForm
    template_name = 'games/quizes/create_quiz.html'

    def form_valid(self, form):
        form.instance.author = self.request.user.profiles
        question_count = self.request.POST.get('question_count')

        if question_count:
            quiz = form.save()
            return redirect(reverse('add-questions', kwargs={
                'quiz_id': quiz.id,
                'count': int(question_count),
            }))
        return super().form_invalid(form)


class AddQuestionsView(View):
    template_name = 'games/quizes/add_questions.html'

    def get(self, request, quiz_id, count):
        try:
            count = int(count)
            if count < 1 or count > 100:
                raise ValueError
        except ValueError:
            raise Http404()

        quiz = get_object_or_404(Quiz, id=quiz_id)
        return render(request, self.template_name, {
            'quiz': quiz,
            'count': count,
            'question_range': range(1, count + 1),
        })

    def post(self, request, quiz_id, count):
        try:
            count = int(count)
            if count < 1 or count > 100:
                raise ValueError
        except ValueError:
            raise Http404()

        quiz = get_object_or_404(Quiz, id=quiz_id)

        for i in range(1, count + 1):
            text = request.POST.get(f'question_{i}')
            a = request.POST.get(f'a_{i}')
            b = request.POST.get(f'b_{i}')
            c = request.POST.get(f'c_{i}')
            d = request.POST.get(f'd_{i}')
            correct = request.POST.get(f'correct_{i}')

            if text and a and b and c and d and correct:
                Question.objects.create(
                    quiz=quiz,
                    text=text[:500],
                    option_a=a[:255],
                    option_b=b[:255],
                    option_c=c[:255],
                    option_d=d[:255],
                    correct_answer=correct
                )

        return redirect('home')


class QuizesView(ListView):
    model = Quiz
    context_object_name = 'quizes'
    template_name = 'games/quizes/games.html'

class QuizesDetailView(DetailView):
    model = Quiz
    template_name = 'games/quizes/quiz.html'
    context_object_name = 'quiz'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'


class QuizAnswersView(View):
    def post(self, request, slug):
        quiz = get_object_or_404(Quiz, slug=slug)

        total_questions = quiz.questions.count()
        correct_count = 0

        for question in quiz.questions.all():
            submitted_answer = request.POST.get(f'question_{question.pk}')
            if submitted_answer == question.correct_answer:
                correct_count += 1

        score = (correct_count / total_questions) * 100 if total_questions > 0 else 0

        attempt, created = QuizAttempt.objects.get_or_create(
            profile=request.user.profiles,
            quiz=quiz,
            defaults={'score': score, 'time_completion': now()}
        )
        if not created:
            if attempt.score < score:
                attempt.score = score
                attempt.time_completion = now()
                attempt.save()

        leaderboard = QuizAttempt.objects.filter(quiz=quiz).order_by('-score', 'time_completion')

        return render(request, 'games/quizes/quiz_answers.html', {
            'quiz': quiz,
            'score': score,
            'total_questions': total_questions,
            'correct_count': correct_count,
            'leaderboard': leaderboard,
        })
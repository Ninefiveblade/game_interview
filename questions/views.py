from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView

from .models import Answer, Result, Test, Question


@login_required
def index(request):
    template = 'questions/index.html'
    tests = Test.objects.all()
    context = {
        'tests': tests,
    }
    return render(request, template, context)


class TestView(DetailView):
    template_name = 'questions/questions.html'
    context_object_name = 'test'

    def get_queryset(self):
        """Вернуть 2 последних свежих опроса"""
        return Test.objects.all()


def vote(request, pk):
    test = Test.objects.get(id=pk)
    print(request.POST)
    if request.POST.get('answer'):
        selected_answers = Answer.objects.filter(id=request.POST['answer'])
        storage_answers = {}
        for answer in selected_answers:
            answer.vote = 0
            print(answer.vote)
            storage_answers[answer.answer] = [answer.correct]
            if storage_answers[answer.answer][0]:
                answer.vote += 1
                print(answer.vote)
                answer.save()
            else:
                template = 'questions/questions.html'
                context = {
                    'error_message': f'Ваш ответ: {answer.answer} неверный',
                    'correct_test': f'Правильные ответы:{test.questions.filter(answers__correct=True)}'
                }
                return render(request, template, context)
        return redirect('questions:result', pk)
    else:
        selected_answers = Answer.objects.filter(id=request.POST['answer'])


class ResultsView(DetailView):
    model = Result
    template_name = 'questions/results.html'
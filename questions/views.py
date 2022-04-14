from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.views.generic.detail import DetailView

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
    template_name = 'questions/test.html'
    context_object_name = 'test'

    def get_object(self):
        test_id = self.kwargs.get('pk')
        return Test.objects.get(pk=test_id)


def question(request, question_id):
    question = Question.objects.get(pk=question_id)
    test = question.test_id.questions.values_list('id')
    last_question_id = list(test)[-1][0]
    correct_answer = question.answers.filter(correct=True).count()
    template_name = 'questions/question.html'
    context = {
        "question": question,
        "correct_answer": correct_answer,
        "last_question_id": last_question_id
    }
    return render(request, template_name, context)


def vote(request, pk):
    q = Question.objects.get(id=pk)
    if request.method == 'POST':
        answers_id = request.POST.getlist('answer')
        for answer in answers_id:
            answer = Answer.objects.get(id=answer)
            if Answer.objects.get(id=answer).correct:
                answer.vote += 1
                answer.correct = Answer.objects.get(id=answer).correct
            else:
                answer.vote -= 1
                answer.correct = Answer.objects.get(id=answer).correct
            answer.user = request.user
            answer.save()
            return redirect('questions:question', pk+1)
    # сохранили ответ в базу, заодно проверили правильный ли ответ
    # return redirect(reverse("question", id=get_next_id(question_id)))
    # где get_next_id может опирать на какое-нибудь поле в Question, например
    # при создании объекта вопроса мы указываем его порядковый номер


class ResultsView(DetailView):
    model = Result
    template_name = 'questions/results.html'

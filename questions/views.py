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
        count = 0
        for answer in answers_id:
            if Answer.objects.get(id=answer).correct:
                answer = Answer.objects.get(id=answer)
                count += 10
                answer.vote += 1
            else:
                answer = Answer.objects.get(id=answer)
                count -= 10
                answer.vote += 1
            Result.objects.update(
                id=29,
                result_rating=count,
                user=request.user,
                test_id=q.test_id
            )
            return redirect('questions:question', pk+1)
        print(count)
        return redirect('questions:result', q.test_id.id)


def results(request, test_id):
    result = Result.objects.filter(test_id=test_id)
    print(result)
    template = 'questions/results.html'
    context = {
        'results': result,
    }
    return render(request, template, context)

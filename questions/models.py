from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Test(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='Название теста'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тесты'
        verbose_name_plural = 'Тесты'


class Question(models.Model):
    test_id = models.ForeignKey(
        Test,
        on_delete=models.CASCADE,
        related_name='questions'
    )
    question = models.CharField(max_length=100)


class Answer(models.Model):
    question_id = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name='answers'
    )
    answer = models.CharField(max_length=100)
    vote = models.IntegerField(default=0)
    correct = models.BooleanField()

    def __str__(self):
        return self.answer


class Result(models.Model):
    test_id = models.ForeignKey(
        Test,
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    result_rating = models.FloatField()

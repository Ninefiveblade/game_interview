from django.contrib import admin
from .models import Test, Question, Answer, Result


class QuestionsInline(admin.TabularInline):
    model = Answer


@admin.register(Question)
class QuextionAdmin(admin.ModelAdmin):
    inlines = [QuestionsInline]


class QuestionAdmin(admin.ModelAdmin):
    list_display = ("question", "answer")


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ("test_id", "user", "result_rating")

    def has_add_permission(self, request):
        return False


@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ("title",)

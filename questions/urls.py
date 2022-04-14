from django.urls import path
from . import views

app_name = 'questions'

urlpatterns = [
    path('', views.index, name='index'),
    path('test/<int:pk>/', views.TestView.as_view(), name='tests'),
    path(
        'question/<int:question_id>/',
        views.question,
        name='question'
    ),
    path('question/<int:pk>/vote/', views.vote, name='vote'),
    path('results/<int:test_id>/', views.results, name='result')
]

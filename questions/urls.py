from django.urls import path
from . import views

app_name = 'questions'

urlpatterns = [
    path('', views.index, name='index'),
    path('test/<int:pk>/', views.TestView.as_view(), name='tests'),
    path('test/<int:pk>/vote/', views.vote, name='vote'),
    path('results/<int:pk>/', views.ResultsView.as_view(), name='result')
]

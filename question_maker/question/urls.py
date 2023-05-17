from django.urls import path
from question import views

urlpatterns = [
    path('question', views.question, name='question'),
]
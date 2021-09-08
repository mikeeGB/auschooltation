from django.urls import path
from .views import heart_tones_question_1, heart_tones_question_2

urlpatterns = [
    path('heart_tones/q1', heart_tones_question_1, name='heart_tones_q1'),
    path('heart_tones/q2', heart_tones_question_2, name='heart_tones_q2'),

]

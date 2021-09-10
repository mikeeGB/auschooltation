from django.urls import path
from .views import heart_tones_question_1, heart_tones_question_2, heart_tones_question_3, courses_page

urlpatterns = [
    path('heart_tones/q1', heart_tones_question_1, name='heart_tones_q1'),
    path('heart_tones/q2', heart_tones_question_2, name='heart_tones_q2'),
    path('heart_tones/q3', heart_tones_question_3, name='heart_tones_q3'),
    path('courses/', courses_page, name='courses'),

]

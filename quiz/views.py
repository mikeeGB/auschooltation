from django.shortcuts import render, redirect
from .forms import QuestionForm
from .models import UserAnswer, Question
from .question_options import heart_tones_questions


# Create your views here.
def heart_tones_question_1(request):
    question = Question.objects.get(id=1)
    if request.method == 'POST':
        print(request.POST)
        q1_form = QuestionForm(heart_tones_questions.HEART_TONE_1_CHOICES, request.POST)
        if q1_form.is_valid():
            current_user = request.user
            answer = q1_form.cleaned_data['options']
            ua = UserAnswer(user=current_user, question=question, user_answer=answer)
            ua.save()
            return redirect('heart_tones_q2')
    else:
        q1_form = QuestionForm(heart_tones_questions.HEART_TONE_1_CHOICES)
    return render(request, 'quiz/heart_tones_q1.html', {'q1_form': q1_form, 'question': question})


def heart_tones_question_2(request):
    question = Question.objects.get(id=2)
    if request.method == 'POST':
        print(request.POST)
        q2_form = QuestionForm(heart_tones_questions.HEART_TONE_2_CHOICES, request.POST)
        if q2_form.is_valid():
            current_user = request.user
            answer = q2_form.cleaned_data['options']
            ua = UserAnswer(user=current_user, question=question, user_answer=answer)
            ua.save()
            return redirect('heart_tones_q3')
    else:
        q2_form = QuestionForm(heart_tones_questions.HEART_TONE_2_CHOICES)
    return render(request, 'quiz/heart_tones_q2.html', {'q2_form': q2_form, 'question': question})


def heart_tones_question_3(request):
    question = Question.objects.get(id=3)
    if request.method == 'POST':
        print(request.POST)
        q3_form = QuestionForm(heart_tones_questions.HEART_TONE_3_CHOICES, request.POST)
        if q3_form.is_valid():
            current_user = request.user
            answer = q3_form.cleaned_data['options']
            ua = UserAnswer(user=current_user, question=question, user_answer=answer)
            ua.save()
            return redirect('heart_tones_q4')
    else:
        q3_form = QuestionForm(heart_tones_questions.HEART_TONE_3_CHOICES)
    return render(request, 'quiz/heart_tones_q3.html', {'q3_form': q3_form, 'question': question})


def heart_tones_question_4(request):
    question = Question.objects.get(id=4)
    if request.method == 'POST':
        print(request.POST)
        q4_form = QuestionForm(heart_tones_questions.HEART_TONE_4_CHOICES, request.POST)
        if q4_form.is_valid():
            current_user = request.user
            answer = q4_form.cleaned_data['options']
            ua = UserAnswer(user=current_user, question=question, user_answer=answer)
            ua.save()
            return redirect('heart_tones_q5')
    else:
        q4_form = QuestionForm(options_list=heart_tones_questions.HEART_TONE_4_CHOICES)
    return render(request, 'quiz/heart_tones_q4.html', {'q4_form': q4_form, 'question': question})


def heart_tones_question_5(request):
    question = Question.objects.get(id=5)
    if request.method == 'POST':
        print(request.POST)
        q5_form = QuestionForm(heart_tones_questions.HEART_TONE_5_CHOICES, request.POST)
        if q5_form.is_valid():
            current_user = request.user
            answer = q5_form.cleaned_data['options']
            ua = UserAnswer(user=current_user, question=question, user_answer=answer)
            ua.save()
            return redirect('heart_tones_q6')
    else:
        q5_form = QuestionForm(options_list=heart_tones_questions.HEART_TONE_5_CHOICES)
    return render(request, 'quiz/heart_tones_q5.html', {'q5_form': q5_form, 'question': question})


def heart_tones_question_6(request):
    question = Question.objects.get(id=6)
    if request.method == 'POST':
        print(request.POST)
        q6_form = QuestionForm(heart_tones_questions.HEART_TONE_6_CHOICES, request.POST)
        if q6_form.is_valid():
            current_user = request.user
            answer = q6_form.cleaned_data['options']
            ua = UserAnswer(user=current_user, question=question, user_answer=answer)
            ua.save()
            return redirect('heart_tones_q7')
    else:
        q6_form = QuestionForm(options_list=heart_tones_questions.HEART_TONE_6_CHOICES)
    return render(request, 'quiz/heart_tones_q6.html', {'q6_form': q6_form, 'question': question})


def heart_tones_question_7(request):
    question = Question.objects.get(id=7)
    if request.method == 'POST':
        print(request.POST)
        q7_form = QuestionForm(heart_tones_questions.HEART_TONE_7_CHOICES, request.POST)
        if q7_form.is_valid():
            current_user = request.user
            answer = q7_form.cleaned_data['options']
            ua = UserAnswer(user=current_user, question=question, user_answer=answer)
            ua.save()
            return redirect('heart_tones_q8')
    else:
        q7_form = QuestionForm(options_list=heart_tones_questions.HEART_TONE_7_CHOICES)
    return render(request, 'quiz/heart_tones_q7.html', {'q7_form': q7_form, 'question': question})


def heart_tones_question_8(request):
    question = Question.objects.get(id=8)
    if request.method == 'POST':
        print(request.POST)
        q8_form = QuestionForm(heart_tones_questions.HEART_TONE_8_CHOICES, request.POST)
        if q8_form.is_valid():
            current_user = request.user
            answer = q8_form.cleaned_data['options']
            ua = UserAnswer(user=current_user, question=question, user_answer=answer)
            ua.save()
            return redirect('heart_tones_q9')
    else:
        q8_form = QuestionForm(options_list=heart_tones_questions.HEART_TONE_8_CHOICES)
    return render(request, 'quiz/heart_tones_q8.html', {'q8_form': q8_form, 'question': question})


def heart_tones_question_9(request):
    question = Question.objects.get(id=9)
    if request.method == 'POST':
        print(request.POST)
        q9_form = QuestionForm(heart_tones_questions.HEART_TONE_9_CHOICES, request.POST)
        if q9_form.is_valid():
            current_user = request.user
            answer = q9_form.cleaned_data['options']
            ua = UserAnswer(user=current_user, question=question, user_answer=answer)
            ua.save()
            return redirect('heart_tones_q10')
    else:
        q9_form = QuestionForm(options_list=heart_tones_questions.HEART_TONE_9_CHOICES)
    return render(request, 'quiz/heart_tones_q9.html', {'q9_form': q9_form, 'question': question})


def heart_tones_question_10(request):
    question = Question.objects.get(id=10)
    if request.method == 'POST':
        print(request.POST)
        q10_form = QuestionForm(heart_tones_questions.HEART_TONE_10_CHOICES, request.POST)
        if q10_form.is_valid():
            current_user = request.user
            answer = q10_form.cleaned_data['options']
            ua = UserAnswer(user=current_user, question=question, user_answer=answer)
            ua.save()
            return redirect('profile')
    else:
        q10_form = QuestionForm(options_list=heart_tones_questions.HEART_TONE_9_CHOICES)
    return render(request, 'quiz/heart_tones_q10.html', {'q10_form': q10_form, 'question': question})


def courses_page(request):
    return render(request, 'quiz/courses.html')
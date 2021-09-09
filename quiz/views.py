from django.shortcuts import render, redirect
from .forms import QuestionFormHT1, QuestionFormHT2, QuestionFormHT3
from .models import UserAnswer, Question


# Create your views here.
def heart_tones_question_1(request):
    question = Question.objects.get(id=1)
    if request.method == 'POST':
        print(request.POST)
        q1_form = QuestionFormHT1(request.POST)
        if q1_form.is_valid():
            current_user = request.user
            answer = request.POST['ht_q1_options']
            ua = UserAnswer(user=current_user, question=question, user_answer=answer)
            ua.save()
            return redirect('heart_tones_q2')
    else:
        q1_form = QuestionFormHT1()
    return render(request, 'quiz/heart_tones_q1.html', {'q1_form': q1_form, 'question': question})


def heart_tones_question_2(request):
    question = Question.objects.get(id=2)
    if request.method == 'POST':
        print(request.POST)
        q2_form = QuestionFormHT2(request.POST)
        if q2_form.is_valid():
            current_user = request.user
            answer = request.POST['ht_q2_options']
            ua = UserAnswer(user=current_user, question=question, user_answer=answer)
            ua.save()
            return redirect('heart_tones_q3')
    else:
        q2_form = QuestionFormHT2()
    return render(request, 'quiz/heart_tones_q2.html', {'q2_form': q2_form, 'question': question})


def heart_tones_question_3(request):
    question = Question.objects.get(id=3)
    if request.method == 'POST':
        print(request.POST)
        q3_form = QuestionFormHT3(request.POST)
        if q3_form.is_valid():
            current_user = request.user
            answer = request.POST['ht_q3_options']
            ua = UserAnswer(user=current_user, question=question, user_answer=answer)
            ua.save()
            return redirect('auschool-home')
    else:
        q3_form = QuestionFormHT3()
    return render(request, 'quiz/heart_tones_q3.html', {'q3_form': q3_form, 'question': question})

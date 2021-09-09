from django import forms
from .question_options import heart_tones_questions


class QuestionFormHT1(forms.Form):
    ht_q1_options = forms.CharField(label='Вопрос 1',
                                    widget=forms.RadioSelect(choices=heart_tones_questions.HEART_TONE_1_CHOICES))


class QuestionFormHT2(forms.Form):
    ht_q2_options = forms.CharField(label='Вопрос 2',
                                    widget=forms.RadioSelect(choices=heart_tones_questions.HEART_TONE_2_CHOICES))


class QuestionFormHT3(forms.Form):
    ht_q3_options = forms.CharField(label='Вопрос 3',
                                    widget=forms.RadioSelect(choices=heart_tones_questions.HEART_TONE_3_CHOICES))

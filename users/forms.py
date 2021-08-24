from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User  # model to interact with by the form
        fields = ('username', 'email', 'password1', 'password2')  # fields in the form

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm


# Create your views here.
def register(request):
    error_dict = {}
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            username = user_form.cleaned_data.get('username')
            messages.success(request, f"Аккаунт создан для {username}!")
            return redirect('auschool-home')
        else:
            error_dict['errors'] = user_form.errors
    else:
        user_form = UserRegisterForm(request.POST)
    return render(request, 'users/login_signup.html', {'user_form': user_form, 'error_dict': error_dict})

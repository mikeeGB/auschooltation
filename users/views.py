from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from .forms import UserLogInForm


# Create your views here.
def register_or_log_in(request):
    error_dict = {}
    if request.method == 'POST' and request.POST.get('submit') == 'reg':
        print(request.POST)
        user_reg_form = UserRegisterForm(request.POST)
        if user_reg_form.is_valid():
            user_reg_form.save()
            username = user_reg_form.cleaned_data.get('username')
            messages.success(request, f"Аккаунт создан для {username}!")
            return redirect('auschool-home')
        else:
            error_dict['errors_reg'] = user_reg_form.errors
    else:
        user_reg_form = UserRegisterForm()

    if request.method == 'POST' and request.POST.get('submit') == 'log_in':
        user_log_in_form = UserLogInForm(data=request.POST)
        if user_log_in_form.is_valid():
            print(request.POST)
        else:
            error_dict['log_in_errors'] = user_log_in_form.errors
    else:
        user_log_in_form = UserLogInForm()

    return render(request, 'users/login_signup.html', {'user_reg_form': user_reg_form, 'error_dict': error_dict,
                                                       'user_log_in_form': user_log_in_form})

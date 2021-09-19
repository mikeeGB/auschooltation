from django.shortcuts import render


# Create your views here.
def heart_basics(request):
    return render(request, 'lessons/heart_basics.html')


def heart_norm(request):
    return render(request, 'lessons/heart_norm.html')

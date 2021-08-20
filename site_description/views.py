from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'site_description/home_landing.html')

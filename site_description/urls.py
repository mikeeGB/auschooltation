from django.urls import path
from .views import home, about

urlpatterns = [
    path('', home, name='auschool-home'),
    path('about/', about, name='auschool-about')
]

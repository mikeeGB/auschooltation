from django.contrib import admin
from .models import Questions, Answers, Sections

# Register your models here.
admin.site.register(Questions)
admin.site.register(Answers)
admin.site.register(Sections)

from django.db import models
from quiz.models import UserAnswer


# Create your models here.
class UserProfileStat(models.Model):
    user_answer = models.ForeignKey(UserAnswer, on_delete=models.CASCADE)
    is_correct_answer = models.BooleanField()

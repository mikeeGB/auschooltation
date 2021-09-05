from django.db import models


# Create your models here.
class Questions(models.Model):
    section = models.ForeignKey('Sections', default='Section', on_delete=models.SET_DEFAULT)
    question_text = models.TextField()
    question_audio = models.FileField(upload_to='question_audio')

    class Meta:
        verbose_name = "Question"
        verbose_name_plural = "Questions"

    def __str__(self):
        return f"Question: {self.question_text}"


class Answers(models.Model):
    question = models.OneToOneField(Questions, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=60)

    class Meta:
        verbose_name = "Answer"
        verbose_name_plural = "Answers"

    def __str__(self):
        return f"Answer: {self.answer_text}"


class Sections(models.Model):
    section_name = models.CharField(max_length=15)

    class Meta:
        verbose_name = "Section"
        verbose_name_plural = "Sections"

    def __str__(self):
        return f"Section: {self.section_name}"

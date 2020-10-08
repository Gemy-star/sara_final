from django.db import models
from users.models import User


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='الإسم', blank=True, null=True)
    description = models.CharField(max_length=255, verbose_name='وصف الإمتحان', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class Exam(models.Model):
    name = models.CharField(max_length=255, verbose_name='الإسم', blank=True, null=True)
    TotalResult = models.IntegerField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'exam'
        verbose_name_plural = 'exams'


class Question(models.Model):
    QType = [
        (1, 'اختيار من متعدد'),
        (2, 'مقالى')
    ]
    questionType = models.IntegerField(max_length=255, verbose_name='نوع السؤال', blank=True, choices=QType)
    question = models.CharField(max_length=255, verbose_name='السؤال', blank=True, null=True)
    answer = models.CharField(max_length=255, verbose_name='الإجابة', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    Exam = models.ForeignKey(Exam, on_delete=models.CASCADE)

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'


class FinalResult(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    result = models.IntegerField(verbose_name='النتيجه النهائيه')

    def __str__(self):
        return self.user.first_name

    class Meta:
        verbose_name = 'FinalResult'
        verbose_name_plural = 'FinalResults'

from django.db import models
from django.urls import reverse

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

    Question_number = [
        (20, '20'),
        (25, '25'),
        (30, '30'),
        (50, '50'),
        (100, '100'),

    ]
    question_number = models.SmallIntegerField(null=True, blank=True, choices=Question_number)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('exam-detail', args=[str(self.id)])

    def __str__(self):
         return str(self.name)

    class Meta:
        verbose_name = 'exam'
        verbose_name_plural = 'exams'


class Question(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    marks = models.PositiveIntegerField(default=0)
    question = models.TextField(max_length=500)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    choose = [('A', 'option1'), ('B', 'option2'), ('C', 'option3'), ('D', 'option4')]
    answer = models.CharField(max_length=1, choices=choose)

    def __str__(self):
        return str(self.question)

    def get_absolute_url(self):
        return reverse('question-detail', args=[str(self.id)])

    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'


class FinalResult(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    no_ques_attempt = models.Count
    no_ques_unattempt = models.Count
    no_ques_right = models.Count
    no_ques_wrong = models.Count
    total = models.Count

    def __str__(self):
        return self.user.first_name

    class Meta:
        verbose_name = 'FinalResult'
        verbose_name_plural = 'FinalResults'


class Set(models.Model):
    set_no = models.PositiveIntegerField(default=0)
    ques = models.ManyToManyField(Question)
    no_of_question = models.Count(Question.question)
    exam_name = models.ForeignKey(Exam, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.set_no)

    class Meta:
        verbose_name = 'set'
        verbose_name_plural = 'sets'

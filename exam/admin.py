from django.contrib import admin
from . import models


admin.site.register(models.Category)

admin.site.register(models.Exam)

admin.site.register(models.Question)

admin.site.register(models.Set)

admin.site.register(models.FinalResult)


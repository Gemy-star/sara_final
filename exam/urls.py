from django.urls import path
from . import views

urlpatterns = [
    path('create/exam', views.create_exam, name='create-exam-page'),
    path('create/question', views.create_question, name='create-question-page'),
     path('create/result', views.create_result, name='create-result-page'),
    path('cat/list', views.cat_list, name='cat-list-page'),
    path('list', views.exam_list, name='exam-list-page'),
    path('list/user/<int:pk>', views.exam_list_user, name='exam-user-list-page'),
    path('questions/list/<int:pk>', views.question_list_user, name='question-exam-list-page'),

]

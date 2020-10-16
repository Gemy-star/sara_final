from django.urls import path
from . import views

urlpatterns = [
    path('cat/list', views.cat_list, name='cat-list'),
    path('cat/create', views.create_cat, name='cat-create'),
    path('cat/detail/<int:pk>', views.cat_detail, name='cat-detail'),
    path('cat/update/<int:pk>', views.cat_edit, name='cat-update'),
    path('cat/delete/<int:pk>', views.DeleteCatView.as_view(), name='cat-delete'),
    path('detail/<int:pk>', views.detail_exam, name='exam-detail'),
    path('list/', views.ListExamView.as_view(), name='exam-list'),
    path('update/<int:pk>', views.UpdateExamView.as_view(), name='exam-update'),
    path('create', views.CreateExamView.as_view(), name='exam-create'),
    path('delete/<int:pk>', views.DeleteExamView.as_view(), name='exam-delete'),
    path('question/detail/<int:pk>', views.detail_question, name='question-detail'),
    path('question/list/', views.ListQuestionView.as_view(), name='question-list'),
    path('question/update/<int:pk>', views.UpdateQuestionView.as_view(), name='question-update'),
    path('question/create', views.CreateQuestionView.as_view(), name='question-create'),
    path('question/delete/<int:pk>', views.DeleteQuestionView.as_view(), name='question-delete'),

]

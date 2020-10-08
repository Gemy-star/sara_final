from django.urls import path
from . import views


urlpatterns = [
    path('login', views.loginPage, name='login'),
    path('logout', views.logoutUser, name='logout'),
    path('register', views.register, name='register'),
    path('profile', views.user_detail, name='user-profile'),
    path('detail/<int:pk>', views.detail, name='user-detail'),

]
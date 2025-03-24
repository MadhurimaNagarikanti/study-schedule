from django.urls import path
from . import views
from .views import create_task, task_list

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup, name='signup'),
    path('forget-password/', views.forget_password, name='forget_password'),
    path('home/', views.home, name='home'),
    path('tasks/new/', create_task, name='create_task'),
    path('tasks/', task_list, name='task_list'),
    path("home/help/", views.help_page, name="help"), 
    path('home/profile/', views.profile, name='profile'),
    path('home/settings/', views.settings, name='settings'),
    
]


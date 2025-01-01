from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home route
    path('tasks/', views.task_list, name = 'task_list' ), # Task list route
]

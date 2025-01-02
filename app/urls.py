from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home route
    path('tasks/', views.task_list, name = 'task_list'), # Task list route
    path('tasks/add', views.add_task, name = 'add_task'),
    path('tasks/edit/<int:id>', views.edit_task, name = 'edit_task'),
]

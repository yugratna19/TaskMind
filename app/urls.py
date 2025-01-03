from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home 
    path('tasks/', views.task_list, name = 'task_list'), # Task list 
    path('tasks/add', views.add_task, name = 'add_task'), # Add Tasks
    path('tasks/edit/<int:id>', views.edit_task, name = 'edit_task'), # Edit Tasks
    path('tasks/details/<int:id>', views.task_details, name = 'task_details'), # Details in a Task
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home
    path('tasks/', views.task_list, name='task_list'),  # Task list
    path('tasks/add/', views.add_task, name='add_task'),  # Add Tasks 
    path('tasks/edit/<int:id>/', views.edit_task, name='edit_task'),  # Edit Tasks 
    path('tasks/details/<int:id>/', views.task_details, name='task_details'),  # Details in a Task 
    path('tasks/delete/<int:id>/', views.delete_task, name='delete_task'),  # Delete a Task 
    path('tasks/<int:id>/mark_complete/', views.mark_complete, name='mark_complete'),  # Mark Task as complete 
]

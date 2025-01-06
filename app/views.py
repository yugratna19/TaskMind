from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from .forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator
# Create your views here.


def home(request):
    return render(request, 'home.html')

def task_list(request):
    search_query = request.GET.get('search', '')
    status_filter = request.GET.get('status', '')  # Get status filter from the query parameters
    
    # Filter tasks based on search query
    if search_query:
        tasks = Task.objects.filter(title__icontains=search_query)
    else:
        tasks = Task.objects.all()

    # Apply status filter if provided
    if status_filter:
        tasks = tasks.filter(status=status_filter)

    # Pagination logic
    paginator = Paginator(tasks, 10)  # Show 10 tasks per page
    page_number = request.GET.get('page')  # Get the page number from the URL
    page_obj = paginator.get_page(page_number)

    # Pass the filtered and paginated tasks to the template
    return render(request, 'tasks.html', {'page_obj': page_obj, 'search_query': search_query, 'status_filter': status_filter})

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task has been successfully added!')
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'add_task.html', {'form': form})


def edit_task(request, id):
    task = get_object_or_404(Task, id=id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task has been successfully updated!')
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'edit_task.html', {'form': form})


def delete_task(request, id):
    task = get_object_or_404(Task, id=id)
    task.delete()
    messages.success(request, 'Task has been successfully deleted!')
    return redirect('task_list')


def task_details(request, id):
    task = get_object_or_404(Task, id=id)
    return render(request, 'task_details.html', {'task': task})


def mark_complete(request, id):
    task = get_object_or_404(Task, id=id)
    # Toggle the task's status between 'Completed' and 'Not Completed'
    if task.status == Task.COMPLETED:
        task.status = Task.NOT_COMPLETED
    else:
        task.status = Task.COMPLETED
    task.save()
    messages.success(request, f'Task {id} status has been updated!')
    # Redirect to the task details page after updating the status
    return redirect('task_list' )

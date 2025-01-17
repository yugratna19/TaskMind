from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from .forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q, Case, When, Value, IntegerField

# Create your views here.
def home(request):
    return render(request, 'home.html')

def task_list(request):
    search_query = request.GET.get('search', '')  # Get search query from the request
    status_filter = request.GET.get('status', '')  # Get status filter from the query parameters
    sort_by = request.GET.get('sort_by', '')  # Get sorting option from query parameters
    
    # Filter tasks based on search query for both title and description
    tasks = Task.objects.all()
    if search_query:
        tasks = tasks.filter(
            Q(title__icontains=search_query) | Q(description__icontains=search_query)
        )

    # Apply status filter if provided
    if status_filter:
        tasks = tasks.filter(status=status_filter)

    # Sorting logic based on user selection
    if sort_by == 'priority':
        tasks = tasks.annotate(
            priority_order=Case(
                When(priority='High', then=Value(1)),
                When(priority='Medium', then=Value(2)),
                When(priority='Low', then=Value(3)),
                default=Value(4),
                output_field=IntegerField()
            )
        ).order_by('priority_order', 'title')
    elif sort_by == 'due_date':
        tasks = tasks.order_by('due_date', 'title')
    elif sort_by == 'status':
        tasks = tasks.order_by('status', 'title')
    else:
        tasks = tasks.order_by('title')  # Default: Sort alphabetically by title

    # Pagination logic
    paginator = Paginator(tasks, 9)  # Show 9 tasks per page
    page_number = request.GET.get('page')  # Get the page number from the URL
    page_obj = paginator.get_page(page_number)

    # Pass the filtered and paginated tasks to the template
    return render(request, 'tasks.html', {
        'page_obj': page_obj,
        'search_query': search_query,
        'status_filter': status_filter,
        'sort_by': sort_by
    })

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task has been successfully added!')
            return redirect('task_list')
        else:
            messages.error(
                request, 'Error in the form. Please correct the errors and try again')
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
            messages.error(
                request, 'Error in the form. Please correct the errors and try again')
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
    return redirect('task_list')

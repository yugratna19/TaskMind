from django.shortcuts import render
from .models import Task
from .forms import TaskForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def task_list (request):
    tasks = [
        {"title": "Study Django", "description": "Work on the TaskMind project", "due_date": "2025-01-02"},
        {"title": "Workout", "description": "Follow workout routine", "due_date": "2025-01-02"},
    ]
    return render(request, 'task.html',{'tasks':tasks}) 

def add_task(request):
    if request.method == 'Post':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
    else: 
        form = TaskForm()
    return render (request, 'add_task.html',{'form': form})

def edit_task(request,id):
    task = Task.objects.get(id =id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance= task)
        if form.is_valid():
            form.save()
    else: 
        form = TaskForm(instance= task)
    return render (request, 'edit_task.html',{'form': form})


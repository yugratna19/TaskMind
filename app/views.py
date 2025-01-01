from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def task_list (request):
    tasks = [
        {"title": "Study Django", "description": "Work on the TaskMind project", "due_date": "2025-01-02"},
        {"title": "Workout", "description": "Follow workout routine", "due_date": "2025-01-02"},
    ]
    return render(request, 'task.html',{'tasks':tasks}) 
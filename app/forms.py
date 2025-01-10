from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'status', 'priority']  # Add 'priority' to fields
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),  # Date picker for due_date
            'priority': forms.Select(attrs={'class': 'form-control'})  # Dropdown for priority
        }

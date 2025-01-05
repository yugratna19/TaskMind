from django.db import models

class Task(models.Model):
    NOT_COMPLETED = 'Not Completed'
    COMPLETED = 'Completed'
    STATUS_CHOICES = [
        (NOT_COMPLETED, 'Not Completed'),
        (COMPLETED, 'Completed'),
    ]

    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=NOT_COMPLETED)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    # Optional: Provide a human-readable representation of the task's status
    def get_status_display(self):
        return dict(self.STATUS_CHOICES).get(self.status, self.status)

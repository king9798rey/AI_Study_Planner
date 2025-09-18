from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class StudyPlan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    target_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[('active', 'Active'), ('completed', 'Completed')], default='active')
    total_hours = models.IntegerField(default=0)
    

    def __str__(self):
        return self.name
    

class Subject(models.Model):
    
    studyplan = models.ForeignKey(StudyPlan, on_delete=models.CASCADE, related_name='subjects')
    name = models.CharField(max_length=100)
    subject_priority =models.IntegerField(default=1)
    allocated_hours = models.IntegerField(default=0)
    completed_hours = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    
class Task(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    due_date = models.DateField()
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

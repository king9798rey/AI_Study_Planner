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
    
    def progress(self):
        if self.allocated_hours == 0:
            return 0
        return (self.completed_hours/self.allocated_hours)*100
    
class Task(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=200)
    allocated_time = models.IntegerField(default=0)
    priority = models.IntegerField(default=1)
    completed_time = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(default='in progress')

    def __str__(self):
        return self.title


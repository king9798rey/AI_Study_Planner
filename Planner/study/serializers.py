from django.contrib.auth.models import User
from rest_framework import serializers
from .models import StudyPlan, Subject, Task

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields = '__all__'
 
class SubjectSerializer(serializers.Serializer):
    class Meta:
        model = Subject
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class StudyPlanSerializer(serializers.ModelSerializer):
    subjects = SubjectSerializer(many=True, read_only=True)
    tasks = TaskSerializer(many=True, read_only=True)

    class Meta:
        model = StudyPlan
        fields = '__all__'

class AnalyticSerializer(serializers.ModelSerializer):
    progress = serializers.SerializerMethodField()
    total_tasks = serializers.SerializerMethodField()
    completed_tasks = serializers.SerializerMethodField()
    pending_tasks = serializers.SerializerMethodField()
    

    class Meta:
        model = Subject
        fields = ['name','progress', 'total_tasks','completed_tasks','pending_tasks','allocated_hours', 'completed_hours',]

    def get_progress(self, obj):
            if obj.allocated_hours==0:
                return 0
            return (obj.completed_hours/obj.allocated_hours)*100
        
    def get_total_tasks(self, obj):
            return obj.tasks.count()
        
    def get_completed_tasks(self, obj):
            return obj.tasks.filter(status='completed').count()

    def get_pending_tasks(self, obj):
            return obj.tasks.exclude(status='completed').count()
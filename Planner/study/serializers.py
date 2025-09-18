from django.contrib.auth.models import User
from rest_framework import serializers
from .models import StudyPlan, Subject, Task

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= User
        fields = '__all__'
 
class SubjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class StudyPlanSerializer(serializers.HyperlinkedModelSerializer):
    subjects = SubjectSerializer(many=True, read_only=True)
    tasks = TaskSerializer(many=True, read_only=True)

    class Meta:
        model = StudyPlan
        fields = ['id', 'user', 'name', 'target_date', 'created_at', 'status', 'total_hours', 'subjects', 'tasks']

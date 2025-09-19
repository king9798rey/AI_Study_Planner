from django.shortcuts import render
from rest_framework import viewsets , permissions
from django.contrib.auth.models import User
from .models import StudyPlan, Subject, Task
from .serializers import StudyPlanSerializer, SubjectSerializer, TaskSerializer , UserSerializer , AnalyticSerializer

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class CurrentUserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class StudyPlanViewSet(viewsets.ModelViewSet):
    queryset = StudyPlan.objects.all()
    serializer_class = StudyPlanSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return StudyPlan.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Subject.objects.filter(studyplan__user=self.request.user)

    def perform_create(self, serializer):
        serializer.save()
    
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(subject__studyplan__user=self.request.user)

    def perform_create(self, serializer):
        serializer.save()

class AnalyticViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A viewset for viewing and editing Subject analytics.

    Attributes:
        queryset (QuerySet): The set of Subject objects to operate on.
        serializer_class (Serializer): The serializer class used for Subject analytics.
        permission_classes (list): List of permission classes that determine access control.

    Requires:
        User to be authenticated to access the endpoints.
    """
    queryset = Subject.objects.all()
    serializer_class = AnalyticSerializer
    permission_classes = [permissions.IsAuthenticated]

from django.urls import path , include
from rest_framework import routers
from .views import UserViewSet
from .views import StudyPlanViewSet, SubjectViewSet, TaskViewSet , AnalyticViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'current_user', UserViewSet, basename='current_user')
router.register(r'studyplans', StudyPlanViewSet, basename='Plan')
router.register(r'subjects', SubjectViewSet, basename='Subjects')
router.register(r'tasks', TaskViewSet, basename='Tasks')
router.register(r'analytics',AnalyticViewSet, basename='analytics')

#router.register(r'api-auth', include('rest_framework.urls', namespace='rest_framework'))


urlpatterns = [
   path('', include(router.urls)),
   path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

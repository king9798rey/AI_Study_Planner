
from django.urls import path , include
from rest_framework import routers
from .views import UserViewSet
from .views import StudyPlanViewSet, SubjectViewSet, TaskViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'current_user', UserViewSet, basename='current_user')
router.register(r'studyplans', StudyPlanViewSet)
router.register(r'subjects', SubjectViewSet)
router.register(r'tasks', TaskViewSet)

#router.register(r'api-auth', include('rest_framework.urls', namespace='rest_framework'))


urlpatterns = [
   path('', include(router.urls)),
   path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

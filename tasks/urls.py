from django.urls import include, path
from rest_framework import routers
from tasks.views import get_tasks, make_payment, TaskViewSet, ProjectViewSet

router = routers.DefaultRouter()
router.register(r'tasks', TaskViewSet)
router.register(r'projects', ProjectViewSet)


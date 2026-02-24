from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ExerciseViewSet, WorkoutTemplateViewSet, WorkoutSessionViewSet, ExerciseLogViewSet

router = DefaultRouter()

router.register(r'exercicios', ExerciseViewSet)
router.register(r'templates', WorkoutTemplateViewSet)
router.register(r'sessoes', WorkoutSessionViewSet)
router.register(r'logs', ExerciseLogViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
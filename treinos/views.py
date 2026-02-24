from django.shortcuts import render

from rest_framework import viewsets
from .models import Exercise, WorkoutTemplate, WorkoutSession, ExerciseLog
from .serializers import ExerciseSerializer, WorkoutTemplateSerializer, WorkoutSessionSerializer, ExerciseLogSerializer


class ExerciseViewSet(viewsets.ModelViewSet):
    queryset = Exercise.objects.all()

    serializer_class = ExerciseSerializer


class WorkoutTemplateViewSet(viewsets.ModelViewSet):
    queryset = WorkoutTemplate.objects.all()

    serializer_class = WorkoutTemplateSerializer


class WorkoutSessionViewSet(viewsets.ModelViewSet):
    queryset = WorkoutSession.objects.all()

    serializer_class = WorkoutSessionSerializer


class ExerciseLogViewSet(viewsets.ModelViewSet):
    queryset = ExerciseLog.objects.all()

    serializer_class = ExerciseLogSerializer